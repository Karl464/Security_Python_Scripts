# General Description

Current scripts are related to security activities, such as web scraping, sniffing, socket connections, fuzzers, and similar tasks.

## Platform Compatibility

| Platform | Script Types |
|----------|--------------|
| **Windows Only** | Scripts using WMI |
| **Linux Only** | Specific fuzzer scripts |
| **Cross-Platform** | Most web scraping and socket scripts |

----------

# Python Version & Environment Management

It is highly recommended to use a **Virtual Environment** to avoid dependency conflicts. Since this system has multiple Python versions installed (3.11, 3.13, and 3.14), use the commands below to ensure you are targeting the correct version.

## 1. Version Identification

Start here to discover what Python is installed and which binary is actually being invoked — before creating environments or changing anything.

### Find the Active Python Binary

#### From inside a script or REPL

```python
import sys
print(sys.executable)
```

#### From the terminal / command line

| Platform | Command | Notes |
| :--- | :--- | :--- |
| **Windows (CMD)** | `where python` | Lists all matches in PATH order |
| **Windows (PowerShell)** | `(Get-Command python).Source` | Shows the resolved executable |
| **macOS / Linux** | `which python3` | First match in PATH |
| **macOS / Linux (all)** | `whereis python` | All known locations |

#### Common default installation paths

| OS | Typical Path |
|----|---|
| **Windows** | `C:\Users\<Username>\AppData\Local\Programs\Python\Python3x\python.exe` |
| **macOS** | `/usr/local/bin/python3` or `/usr/bin/python3` |
| **Linux** | `/usr/bin/python3` |
| **Homebrew (Mac)** | `/opt/homebrew/bin/python3` |

> **Why multiple paths?** It is common to find 3–4 different binaries on one machine:
> 1. **System Python** — pre-installed by the OS (do not modify).
> 2. **Manual Install** — downloaded from python.org.
> 3. **Virtual Environment (`venv`)** — isolated copy per project.
> 4. **Conda / Anaconda** — separate directory structure.

---

### Windows: List All Installed Versions

[Python Releases for Windows | Python.org](https://www.python.org/downloads/windows/)

| Action | Command |
| :--- | :--- |
| List all installed versions | `py -0` |
| List full folder paths (patch level) | `py --list-paths` |
| Check specific patch level (e.g., 3.11.9) | `py -3.11 --version` |

---

## 2. Controlling Version Priority

Once you know what is installed, use these two independent mechanisms to control which version runs. They work on different layers and can be combined.

### Mechanism A — PATH (controls the `python` command)

Windows searches `PATH` directories in order. The **first folder** containing `python.exe` wins.

```
C:\Python\Python311\   ← listed first → python --version → 3.11
C:\Python\Python314\   ← listed second (ignored for plain `python`)
```

#### Setting Global Priority via PATH (Windows)

1. Open **System Properties → Environment Variables**.
2. Under *User variables*, select **Path** and click **Edit**.
3. Move the Python version entries (e.g. 3.11) **above** the `WindowsApps` entry (and above any other Python version):

    ```
    C:\Users\<user>\AppData\Local\Programs\Python\Python311\
    C:\Users\<user>\AppData\Local\Programs\Python\Python311\Scripts\
    ```

4. Click OK, then **restart CMD / PowerShell**.
5. Verify:

    ```powershell
    python --version   # → Python 3.11.x
    where python       # Confirms correct path is first
    ```

> ⚠️ **WindowsApps stub:** `C:\Users\<user>\AppData\Local\Microsoft\WindowsApps\python.exe` is not a real interpreter — it is a Store redirect that opens the Microsoft Store when invoked. If this path appears above your real Python install in PATH, typing `python` will open the Store instead of running a script. Always ensure your Python 3.11 entries sit above it.

---

### Mechanism B — py.ini (controls the `py` launcher)

The `py` launcher is **independent of PATH** and reads its default from:

- `%LOCALAPPDATA%\py.ini` — user-specific (recommended)
- `%PROGRAMDATA%\py.ini` — system-wide

**Open and set the default:**

```powershell
notepad $env:LOCALAPPDATA\py.ini
```

```ini
[defaults]
python=3.11
```

**Result:**

```powershell
py --version     # → Python 3.11  (from py.ini)
py -3.13         # → Python 3.13  (explicit override)
py -3.14         # → Python 3.14  (explicit override)
```

---

### Priority Summary

| Command | Controlled By | How to Change (e.g. 3.11)|
|---------|--------------|---------------|
| `python` | PATH order | Move Python 3.11 entries above others in PATH |
| `py` | `py.ini` | Set `python=3.11` in `py.ini` |
| `py -3.11` | Explicit flag | Always 3.11, ignores py.ini |
| `py -3.14` | Explicit flag | Always 3.14, ignores py.ini |

> ✅ **Key takeaway:** PATH controls `python`. `py.ini` controls `py`. Set both for a fully predictable environment — then use explicit `py -3.x` flags in scripts to be unambiguous regardless of machine config.

### Recommendations

- **Reproducibility baseline:** Set `py.ini` default to 3.11 and move 3.11 to the top of PATH — ensures known-good tool compatibility (e.g., APKiD).
- **Scripts for juniors:** Always use `py -3.11 myscript.py` explicitly rather than relying on defaults. It works regardless of the machine's PATH or py.ini state.
- **Quick reference for juniors:**
  - `python` → whichever version PATH points to (you decide).
  - `py` → 3.11 (set in py.ini).
  - `py -3.14` → always 3.14, no matter what.

---

## 3. Virtual Environment Lifecycle

### A. Create the Environment

| Platform | Command |
|----------|---------|
| **Windows** | `python.exe -m venv myenv` |
| **Windows (target 3.11)** | `py -3.11 -m venv myenv` |
| **Windows (full path)** | `& "C:\Python\Python-3.x.x\python.exe" -m venv myenv` |
| **Linux/macOS** | `python3 -m venv myenv` |

### B. Activate the Environment

| Platform | Command |
|----------|---------|
| **Windows (PowerShell)** | `.\myenv\Scripts\Activate.ps1` |
| **Windows (CMD)** | `.\myenv\Scripts\activate.bat` |
| **Linux/macOS** | `source myenv/bin/activate` |
| **VS Code** | `>Python: Select Interpreter` |

### C. Validate & Cleanup

| Action | Command |
|--------|---------|
| **Validate active interpreter path** | `python -c "import sys; print(sys.executable)"` |
| **Validate installed packages** | `python -m pip list` |
| **Deactivate** | `deactivate` |
| **Delete (Windows)** | `rmdir /s /q myenv` |
| **Delete (Linux/macOS)** | `rm -rf myenv` |

----------

# Dependency Installation

Install only the dependencies required for the specific script you are running.

| Category | Package | Installation Command |
|----------|---------|---------------------|
| **Net Scanner** | Scapy | `pip install scapy` |
| **Web Scraping** | Requests, BeautifulSoup4, lxml | `pip install requests beautifulsoup4 lxml` |
| **Windows Specific** | WMI | `pip install WMI` |
| **Utilities** | Colorama | `pip install colorama` |
| **Development** | Jupyter | `pip install notebook jupyter ipywidgets` |
| **Certificates** | System Certs | `pip install pip-system-certs` |

**Note:** For Jupyter, install the "Jupyter" extension in VS Code (`Ctrl+Shift+X`).

----------

# Useful pip & py Commands Reference

| Description | Command |
|-------------|---------|
| **Find package** | `pip list \| findstr "<package>"` |
| **Show package info** | `pip show <package>` |
| **Export requirements** | `pip freeze > requirements.txt` |
| **Install from file** | `pip install -r requirements.txt` |
| **Targeted install** | `py -3.11 -m pip install <package>` |
| **Run script (3.11)** | `py -3.11 myscript.py` |
| **Run Django (3.11)** | `py -3.11 manage.py runserver` |

## Problem

If you see this error:

```
Error running program 'pip.exe': An Application Control policy blocked this file
```

[Smart App Control Has Blocked Part of This App — Microsoft Support](https://support.microsoft.com/en-us/windows/smart-app-control-has-blocked-part-of-this-app-0729fff1-48bf-4b25-aa97-632fe55ccca2)

Your system has **Application Control Policies** (AppLocker/SmartScreen) that block `pip.exe`, but `python.exe` is allowed. Running pip as a Python module (`python -m pip`) executes through the allowed `python.exe`.

## Solution

**Always use `python -m pip` instead of `pip`**

| Blocked Command | Working Alternative |
|-----------------|---------------------|
| `pip list` | `python -m pip list` |
| `pip install <package>` | `python -m pip install <package>` |
| `pip freeze` | `python -m pip freeze` |
| `pip show <package>` | `python -m pip show <package>` |

----------

# References

| Resource | Link |
|----------|------|
| **YouTube Tutorial** | [Python Virtual Environments](https://www.youtube.com/watch?v=GZbeL5AcTgw&t=121s) |
| **VS Code Docs** | [Python Environments](https://code.visualstudio.com/docs/python/environments) |
| **Real Python Guide** | [Running Scripts](https://realpython.com/run-python-scripts/) |
| **Package Index** | [PyPI](https://pypi.org/) |
| **Python Releases (Windows)** | [python.org/downloads/windows](https://www.python.org/downloads/windows/) |
| **SmartScreen / AppLocker** | [Microsoft Support](https://support.microsoft.com/en-us/windows/smart-app-control-has-blocked-part-of-this-app-0729fff1-48bf-4b25-aa97-632fe55ccca2) |
