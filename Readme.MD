# General description
Current script are related to security activities, like, web scraping, sniffing, socket connection, fuzzer, or similar activities.

Please be aware that some of current code will work only on windows (ex. WMI) and other only on Linux (ex. fuzzer), and some of them in both enviroment.

# Environment preparation

## Create a virtual environment
To star it is recommended to create a virtual environment before installing the required dependencies

Reference: https://www.youtube.com/watch?v=GZbeL5AcTgw&t=121s

### macOS/Linux 

> python3 -m even .venv 

You may need to run first (Ex. Debian-based OSs):
 > sudo apt-get install python3-ven


### Windows 

> python -m venv .venv 

You can also use 
> py -3 -m venv .venv


## Install dependencies
In order to use the scripts you will need to install dependencies. Just install the dependencies required for the script you required.

### Net Scanner - Scapy
[https://scapy.net/](https://scapy.net/)
> pip  install  scapy

### Web Scraping

[https://pypi.org/project/requests/](https://pypi.org/project/requests/)
> pip  install  requests

[https://pypi.org/project/beautifulsoup4/](https://pypi.org/project/beautifulsoup4/)
> pip  install beautifulsoup4

[https://pypi.org/project/lxml/](https://pypi.org/project/lxml/)
> pip  install  lxml

### Windows WMI
> pip  install WMI

### Colorama
> pip install colorama


## Useful pip commands
Reference: https://pip.pypa.io/en/stable/cli/pip/
Commands                          |Description                         |
-------------------------------|-----------------------------|
`pip  install <package>`  |Install Package            |
`pip  list | findstr "droz"` |Find installed package            |
`pip show <package  name>`  |Show information of package            |
 

# References
 

[https://realpython.com/run-python-scripts/](https://realpython.com/run-python-scripts/)

[https://pypi.org/](https://pypi.org/)