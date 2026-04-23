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

### Find the Python Binary Path

Before anything else, know *which* Python binary is actually being invoked.

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
|----|----|
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

Verify installed versions and their exact paths before creating environments.

| Action | Command |
| :--- | :--- |
| List all installed versions | `py -0` |
| List full folder paths (patch level) | `py --list-paths` |
| Check specific patch level (e.g., 3.11.9) | `py -3.11 --version` |
| Set the default Python version — create or edit **`py.ini`** <br> - **User**: `%LOCALAPPDATA%\py.ini` <br> - **System**: `%PROGRAMDATA%\py.ini` | `notepad $env:LOCALAPPDATA\py.ini` <br> `notepad $env:PROGRAMDATA\py.ini` <br><br>**Set content:**<br>`[defaults]`<br>`python=3.11` |

---

## 2. Version Execution Priority

Understanding how Windows resolves which Python runs when you type `python` vs `py` is essential for reproducible environments.

### How `python` is Resolved — PATH Order

Windows searches directories in `PATH` order. The **first folder** containing `python.exe` wins.

**Example:**

```
C:\Python\Python311\   ← listed first → python --version → 3.11
C:\Python\Python314\   ← listed second (ignored)
```

If 3.14 is listed above 3.11, then `python --version` returns 3.14.

**Verify what PATH resolves:**

```powershell
where python          # All matches, in resolution order
(Get-Command python).Source   # First match only
```

### How `py` is Resolved — py Launcher + py.ini

The `py` launcher is **independent of PATH** and reads its default from:

- `%LOCALAPPDATA%\py.ini` — user-specific
- `%PROGRAMDATA%\py.ini` — system-wide

**Example `py.ini`:**

```ini
[defaults]
python=3.11
```

**With this config:**

```powershell
py --version     # → Python 3.11  (from py.ini default)
py -3.13         # → Python 3.13  (explicit override)
py -3.14         # → Python 3.14  (explicit override)
```

### Priority Summary Table

| Command | Who Decides | How to Control |
|---------|-------------|----------------|
| `python` | PATH order | Move desired version's folder above others in PATH |
| `py` | `py.ini` | Edit `py.ini` to set default version |
| `py -3.11` | Explicit | Always runs Python 3.11, ignores py.ini |
| `py -3.14` | Explicit | Always runs Python 3.14, ignores py.ini |

> ✅ **Key takeaway:** PATH controls `python`. `py.ini` controls `py`. Use both together for predictable, reproducible setups.

### Recommendations

- **Reproducibility baseline:** Set `py.ini` default to 3.11 — ensures known-good tool compatibility (e.g., APKiD).
- **Optional PATH adjustment:** If you also want `python` to resolve to 3.11, move 3.11's folder above 3.14 in System PATH.
- **Documentation for juniors:**
  - `python` → whichever version PATH points to (you control this).
  - `py` → 3.11 (set in py.ini).
  - `py -3.14` → always 3.14, regardless of defaults.

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
