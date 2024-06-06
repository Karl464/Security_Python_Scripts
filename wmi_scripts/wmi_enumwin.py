"""
Use this script to list process and service information
Require:
pip install wmi
"""


import wmi

conn = wmi.WMI()
print ("------------------ List WMI Classes: --------------------")
for class_name in conn.classes:
    if 'Win32_NetworkAdapter' in class_name:
        print(class_name)

for class_name in conn.classes:
    if 'Login' in class_name:
        print(class_name)

for class_name in conn.classes:
    if 'Win32_Operating' in class_name:
        print(class_name)


print ("------------------ Win32_NetworkAdapterConfiguration Properties and Methods: --------------------")
properties = wmi.WMI().Win32_NetworkAdapterConfiguration.methods.keys()
for property in properties:
    print(property)

print ("------------------ Win32_NetworkAdapterConfiguration Instances: --------------------")
instances = wmi.WMI().Win32_NetworkAdapterConfiguration()
for instance in instances:
    print(instance)

print ("------------------ Win32_OperatingSystem Instances: --------------------")
instances = wmi.WMI().Win32_OperatingSystem()
for instance in instances:
    print(instance)

try:
    print ("------------------ Win32_NetworkAdapterConfiguration Instances Domains/MAC: --------------------")
    for netParams in wmi.WMI().Win32_NetworkAdapterConfiguration():
        print("Caption: ",netParams.Caption)
        if netParams.MACAddress != None and netParams.IPAddress != None and netParams.IPSubnet != None:
            if netParams.DNSDomainSuffixSearchOrder != None:
                print("Domain: ",netParams.DNSDomainSuffixSearchOrder)
        print("mac: ",netParams.MACAddress)
        print("ip: ",netParams.IPAddress)
        print("mask: ",netParams.IPSubnet)
    
    # print ("------------------ Win32_NetworLoginProfile Instances Domains/MAC: --------------------")
    # for profileparams in wmi.WMI().Win32_NetworLoginProfile():
    #     if profileparams.Name != None:
    #         print("Profile: ",profileparams.Name)
            
    for SOParam in wmi.WMI().Win32_OperatingSystem():
        print("Operation System: ", SOParam.caption)
        print("Computer Name: ", SOParam.CSName)
        print("OSArchitecture: ", SOParam.OSArchitecture)
        print("User Registered: ", SOParam.RegisteredUser)

except Exception as e:
    print(e)