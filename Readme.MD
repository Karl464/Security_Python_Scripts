# General description
Current scripts are related to security activities, like, web scraping, sniffing, socket connection, fuzzer, or similar activities.

Please be aware that some of current code will work only on windows (ex. WMI) and other only on Linux (ex. fuzzer), and some of them in both enviroment.

# Managing Python Virtual Environments

Is recommended to create a virtual environment before installing the required dependencies, As this will help to avoid dependency problems when working with multiple projects.

Reference: https://www.youtube.com/watch?v=GZbeL5AcTgw&t=121s


## Windows

1. **Create a Virtual Environment:**
   ```sh
   python -m venv myenv

2. Activate the Virtual Environment:
    ```sh
    myenv\Scripts\activate

3. Validate the Virtual Environment:

    ```sh
    python -m pip list

4. Deactivate the Virtual Environment:

    ```sh
    deactivate


5. Delete the Virtual Environment: Simply delete the myenv directory:

    ```sh
    rmdir /s /q myenv


## Linux/macOS

1. **Create a Virtual Environment:**
   ```sh
   python3 -m venv myenv


2. Activate the Virtual Environment:
    ```sh
    source myenv/bin/activate


3. Validate the Virtual Environment:

    ```sh
    python -m pip list

4. Deactivate the Virtual Environment:

    ```sh
    deactivate


5. Delete the Virtual Environment: Simply delete the myenv directory:

    ```sh
    rm -rf myenv



## Install dependencies
In order to use the scripts you will need to install dependencies. Just install the dependencies required for the script you required.

### Net Scanner - Scapy
[https://scapy.net/](https://scapy.net/)
    
    pip  install  scapy

### Web Scraping

[https://pypi.org/project/requests/](https://pypi.org/project/requests/)
    
    pip  install  requests

[https://pypi.org/project/beautifulsoup4/](https://pypi.org/project/beautifulsoup4/)

    pip  install beautifulsoup4

[https://pypi.org/project/lxml/](https://pypi.org/project/lxml/)

    pip  install  lxml

### Windows WMI

    pip  install WMI

### Colorama

    pip install colorama


## Useful pip commands
Reference: https://pip.pypa.io/en/stable/cli/pip/


| Description | Commands |
|----------|----------|
| Install Package                |  pip  install &lt;package &gt;  |
| Find installed package         |  pip  list &#124; findstr "&lt;package &gt;" |
| Show information of package    |  pip  show &lt;package &gt;  |


# References
 

[https://realpython.com/run-python-scripts/](https://realpython.com/run-python-scripts/)

[https://pypi.org/](https://pypi.org/)
