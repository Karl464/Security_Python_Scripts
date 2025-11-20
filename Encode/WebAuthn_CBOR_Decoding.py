import base64
import cbor2
import json

# --- 1. INPUT DATA ---
# The Base64URL-encoded attestation object
ATTESTATION_OBJECT_B64U = "o2NmbXRjdHBtZ2F0d..."
CLIENT_DATA_JSON_B64U = "eyJ0eXBlIjoid2ViYXV0aG..."

# Helper function to convert 'bytes' objects to hex strings for JSON serialization
def convert_bytes_to_hex(obj):
    if isinstance(obj, bytes):
        return obj.hex() # Convert the bytes object to a hexadecimal string
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

# Helper function to perform URL-safe Base64 decoding
def decode_base64url(data):
    # Padding is typically omitted in base64url. Add it back for standard decode.
    padding = '=' * (4 - (len(data) % 4) % 4)
    # Convert URL-safe characters back to standard base64 characters
    return base64.urlsafe_b64decode(data + padding)

# --- 2. CBOR DECODING ---
att_obj_bytes = decode_base64url(ATTESTATION_OBJECT_B64U)
att_obj = cbor2.loads(att_obj_bytes)

auth_data_bytes = att_obj['authData']
att_stmt = att_obj['attStmt']

# --- 3. AUTHENTICATOR DATA (authData) PARSING ---

# Constants for authData structure
RP_ID_HASH_LEN = 32
FLAGS_LEN = 1
SIGN_COUNT_LEN = 4
AAGUID_LEN = 16
CRED_ID_LEN_FIELD_LEN = 2 # Length is a 16-bit integer (2 bytes)

# Extract fixed-length fields
rp_id_hash = auth_data_bytes[0:RP_ID_HASH_LEN]
flags = auth_data_bytes[RP_ID_HASH_LEN:RP_ID_HASH_LEN + FLAGS_LEN]
sign_count = auth_data_bytes[RP_ID_HASH_LEN + FLAGS_LEN:RP_ID_HASH_LEN + FLAGS_LEN + SIGN_COUNT_LEN]
current_offset = RP_ID_HASH_LEN + FLAGS_LEN + SIGN_COUNT_LEN

# Determine if Attested Credential Data (ACD) is present (AT flag is 0x40)
AT_FLAG_SET = (flags[0] & 0x40)

# Extract Attested Credential Data (ACD) if present
attested_credential_data = None
cose_public_key = None
credential_id = None
aaguid = None

if AT_FLAG_SET:
    # AAGUID (16 bytes)
    aaguid = auth_data_bytes[current_offset:current_offset + AAGUID_LEN]
    current_offset += AAGUID_LEN

    # Credential ID Length (2 bytes, little-endian)
    cred_id_len_bytes = auth_data_bytes[current_offset:current_offset + CRED_ID_LEN_FIELD_LEN]
    credential_id_length = int.from_bytes(cred_id_len_bytes, byteorder='big')
    current_offset += CRED_ID_LEN_FIELD_LEN

    # Credential ID (Variable length)
    credential_id = auth_data_bytes[current_offset:current_offset + credential_id_length]
    current_offset += credential_id_length
    
    # COSE Public Key (CBOR structure)
    # The rest of the buffer is the CBOR-encoded COSE key
    cose_public_key_bytes = auth_data_bytes[current_offset:]
    cose_public_key = cbor2.loads(cose_public_key_bytes)


# --- 4. PRINT DECODED DATA ---
print("="*60)
print("🔑 CBOR ATTESTATION OBJECT DECODING")
print("="*60)

print("\n## 1. Top-Level Attestation Object")
print(f"  Format (fmt): \033[1m{att_obj['fmt']}\033[0m")
print(f"  AuthData Length: {len(auth_data_bytes)} bytes")
print(f"  Attestation Statement Keys: {list(att_stmt.keys())}")

print("\n" + "-"*60)

print("\n## 2. Attestation Statement (attStmt) - Packed Format")
print(f"  Algorithm (alg): {att_stmt.get('alg')} (COSE -7 = ES256)")
print(f"  TPM Version (ver): {att_stmt.get('ver')}")
print(f"  Signature (sig): {att_stmt['sig'].hex()[:16]}... (Truncated)")
print(f"  Certificate Chain (x5c) Count: {len(att_stmt['x5c'])}")
print(f"  TPM CertInfo: {att_stmt.get('certInfo').hex()[:16]}... (Truncated)")
print(f"  TPM PubArea: {att_stmt.get('pubArea').hex()[:16]}... (Truncated)")

print("\n" + "-"*60)

print("\n## 3. Authenticator Data (authData) - Binary Fields")
print(f"  RP ID Hash: {rp_id_hash.hex()}")
print(f"  Flags Byte: {flags.hex()} (Hex)")
print(f"    - User Present (UP): {'Yes' if (flags[0] & 0x01) else 'No'}")
print(f"    - Attested Data (AT): {'Yes' if AT_FLAG_SET else 'No'}")
print(f"  Sign Count: {int.from_bytes(sign_count, byteorder='big')} ({sign_count.hex()} Hex)")

if AT_FLAG_SET and aaguid and credential_id and cose_public_key:
    print("\n  >>> Attested Credential Data (ACD) <<<")
    print(f"  AAGUID: {aaguid.hex()}")
    print(f"  Credential ID Length: {credential_id_length} bytes")
    print(f"  Credential ID: {credential_id.hex()}")
    
    print("\n  >>> COSE Public Key (CBOR) <<<")
    # Pretty print the CBOR-decoded COSE key (using JSON for formatting)
    print(json.dumps(cose_public_key, indent=4, default=convert_bytes_to_hex))
    print(f"    Key Type (kty): {cose_public_key.get(1)} (2 = EC2)")
    print(f"    Algorithm (alg): {cose_public_key.get(3)} (-7 = ES256)")
    print(f"    Curve (crv): {cose_public_key.get(-1)} (1 = P-256)")
    print(f"    X-Coordinate (x): {cose_public_key.get(-2).hex()} (32 bytes)")
    print(f"    Y-Coordinate (y): {cose_public_key.get(-3).hex()} (32 bytes)")
    
print("\n" + "="*60)
print("✅ Decoding Complete.")
print("="*60)


import hashlib
import json

# Decode clientDataJSON
client_data_json_bytes = decode_base64url(CLIENT_DATA_JSON_B64U)

# Calculate SHA-256 hash
client_data_hash = hashlib.sha256(client_data_json_bytes).digest()

print(f"Client Data Hash (SHA-256): {client_data_hash.hex()}")

# Signature Verification Input = authData + clientDataHash
verification_input = auth_data_bytes + client_data_hash
print(f"Verification Input Buffer Length: {len(verification_input)}")
