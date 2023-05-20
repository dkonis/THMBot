# THMBot
## TryHackMe bot for maintaining your streak

[![Python 3.10.4](https://img.shields.io/badge/python-3.10.4-yellow.svg)](https://www.python.org/)

THMBot is a Selenium powered Python tool,<br />
that automates the process of checking in everyday in TryHackMe.

## Features

- ReCapcha bypass.
- Setup Script that creates a scheduled task and an account configuration.
- The tool's actions and progress are logged.
- Support for Windows and Linux systems.



## Installation

THMBot requires [Python3](https://www.python.org/) and [Firefox](https://www.mozilla.org/en-US/firefox/new/) to run.

Clone the repository:

```sh
git clone https://github.com/dkonis/THMBot.git
```

Install the dependencies form requirements.txt:

```sh
cd THMBot
pip install -r requirements.txt
```

For Windows systems run setup.bat:

```cmd
setup.bat
```

For Linux systems run setup.sh as sudo:<br />
(If you don't have apt you also need to install FFmpeg manualy from [here](https://ffmpeg.org/download.html#build-linux)).

```sh
chmod +x setup.sh
sudo ./setup.sh
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

Set a time for the Scheduled Task to run (Format - HH:MM): <HH:MM>

Please enter the run as password for your computer user: <Computer_Password>
```
And you are set!


## Logging

When THMBot runs, it logs actions and progress in tryhackmebot.log:

```
25-07-2022, 20:38:15
[+] Starting...
[+] Attempting to Solve Recaptcha
[+] Recaptcha Passcode: 3 work becomes critical
[+] Attempting to Solve Recaptcha
[+] Recaptcha Passcode: software applications ranging
[+] You Are Logged In!
[+] Room's Progress Reset
[+] Success! Your Streak is 40
[+] Closing...

26-07-2022, 20:40:27
[+] Starting...
[+] Attempting to Solve Recaptcha
[+] Recaptcha Passcode: is directly is pretty up
[+] You Are Logged In!
[+] Room's Progress Reset
[+] Success! Your Streak is 41
[+] Closing...
```

## Notes

- To uninstall you can use the uninstall.bat script for Windows systems and the uninstall.sh as sudo for Linux systems.<br />Those scripts will revert the project back to the point of cloning, then you can delete the project's folder.
- the scheduled task or Cron Job will not work if you move the project's folder after setup.<br />
If you need to change the location, please use uninstall.bat/sh and run setup.bat/sh after the location has changed.
- Currently you have to join this [room](https://tryhackme.com/room/polkit) to be able to run THMBot (will be fixed soon).
