# THMBot (for educational purpose only)
## TryHackMe bot for maintaining your streak

[![Python 3.10.4](https://img.shields.io/badge/python-3.10.4-yellow.svg)](https://www.python.org/)

THMBot is a Selenium powered Python tool,
that automates the process of checking in everyday in TryHackMe.

## Features

- ReCapcha bypass.
- Setup Script that creates a scheduled task and an account configuration.
- Support for Windows (support for Linux coming soon).



## Installation

THMBot requires [Python 3](https://www.python.org/) to run.

Install the dependencies form requirements.txt:

```sh
cd THMBot
pip install -r requirements.txt
```

For Windows run setup.bat:

```cmd
setup.bat
```
Follow the instructions:

```
88888888888 888    888 888b     d888 888888b.            888
    888     888    888 8888b   d8888 888  "88b           888
    888     888    888 88888b.d88888 888  .88P           888
    888     8888888888 888Y88888P888 8888888K.   .d88b.  888888
    888     888    888 888 Y888P 888 888  "Y88b d88""88b 888
    888     888    888 888  Y8P  888 888    888 888  888 888
    888     888    888 888   "   888 888   d88P Y88..88P Y88b.
    888     888    888 888       888 8888888P"   "Y88P"   "Y888

Set your THM Email: <THM_Mail>
Set your THM password: <THM_Password>

Note: to update your account credentials change -  account.conf 

Set a time for the Scheduled Task to run (Format - 00:00): <HH:MM>

Please enter the run as password for your computer user: <Computer_Password>
```
And you are set!