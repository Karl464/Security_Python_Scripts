
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

## 1. Version Identification (Windows)

[Python Releases for Windows | Python.org](https://www.python.org/downloads/windows/)

Before creating an environment, verify your installed versions and their exact paths.

| Action | Command |
|--------|---------|
| List all installed versions | `py -0` |
| List full folder paths (Patch level) | `py --list-paths` |
| Check specific patch (e.g., 3.11.9) | `py -3.11 --version` |

## 2. Virtual Environment Lifecycle

### A. Create the Environment

| Platform | Command |
|----------|---------|
| **Windows** | `python.exe -m venv myenv` |
| **Windows (Target 3.11)** | `py -3.11 -m venv myenv` |
| **Windows (Full Path)** | `& "C:\Python\Python-3.x.x\python.exe" -m venv myenv` |
| **Linux/macOS** | `python3 -m venv myenv` |

### B. Activate the Environment

| Platform | Command |
|----------|---------|
| **Windows (PowerShell)** | `.\myenv\Scripts\Activate.ps1` |
| **Windows (CMD)** | `.\myenv\Scripts\activate.bat` |
| **Linux/macOS** | `source myenv/bin/activate` |

### C. Validate & Cleanup

| Action | Command |
|--------|---------|
| **Validate Path** | `python -c "import sys; print(sys.executable)"` |
| **Validate Content** | `python -m pip list` |
| **Deactivate** | `deactivate` |
| **Delete (Windows)** | `rmdir /s /q myenv` |
| **Delete (Linux)** | `rm -rf myenv` |

----------

# Dependency Installation

Install only the dependencies required for the specific script you are running.

| Category | Package | Installation Command |
|----------|---------|---------------------|
| **Net Scanner** | Scapy | `pip install scapy` |
| **Web Scraping** | Requests, BeautifulSoup4, lxml | `pip install requests beautifulsoup4 lxml` |
| **Windows Specific** | WMI | `pip install WMI` |
| **Utilities** | Colorama | `pip install colorama` |
| **Development** | Jupyter | `pip install notebook` |
| **Certificates** | System Certs | `pip install pip-system-certs` |

**Note:** For Jupyter, install the "Jupyter" extension in VS Code (Ctrl+Shift+X).

----------

# Useful pip & py Commands Reference

| Description | Command |
|-------------|---------|
| **Find package** | `pip list \| findstr "<package>"` |
| **Show package info** | `pip show <package>` |
| **Export requirements** | `pip freeze > requirements.txt` |
| **Install from file** | `pip install -r requirements.txt` |
| **Targeted Install** | `py -3.11 -m pip install <package>` |
| **Run Script (3.11)** | `py -3.11 myscript.py` |
| **Run Django (3.11)** | `py -3.11 manage.py runserver` |

----------

# References

| Resource | Link |
|----------|------|
| **YouTube Tutorial** | [Python Virtual Environments](https://www.youtube.com/watch?v=GZbeL5AcTgw&t=121s) |
| **VS Code Docs** | [Python Environments](https://code.visualstudio.com/docs/python/environments) |
| **Real Python Guide** | [Running Scripts](https://realpython.com/run-python-scripts/) |
| **Package Index** | [PyPI](https://pypi.org/) |
