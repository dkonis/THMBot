#!/bin/bash

RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${RED} 88888888888 888    888 888b     d888 888888b.            888"
echo -e "     888     888    888 8888b   d8888 888  \"88b           888"
echo -e "     888     888    888 88888b.d88888 888  .88P           888"
echo -e "     888     8888888888 888Y88888P888 8888888K.   .d88b.  888888"
echo -e "     888     888    888 888 Y888P 888 888  \"Y88b d88\"\"88b 888"
echo -e "     888     888    888 888  Y8P  888 888    888 888  888 888"
echo -e "     888     888    888 888   \"   888 888   d88P Y88..88P Y88b."
echo -e "     888     888    888 888       888 8888888P\"   \"Y88P\"   \"Y888${NC}"

echo -e
read -p "Set Your THM Email: " MAIL
read -sp "Set Your THM Password: " PASS

echo [account] > account.conf
echo mail = $MAIL >> account.conf
echo PASS = $PASS >> account.conf

echo -e
echo -e
echo -e "${YELLOW}Note: to update your account credentials change - account.conf${NC}"

echo -e
read -p "Set a time for the Cron Job to run (Format - HH:MM): " CRONTIME

echo -e
echo -e
echo -e "${YELLOW}Note: to update your Cron Job type - crontab -e${NC}"

PART=(${CRONTIME//:/ })

crontab -u $(logname) -l | grep -v '&& python3 main.py'  | crontab -u $(logname) -
crontab -u $(logname) -l |{ cat; echo "${PART[1]} ${PART[0]} * * * cd $(pwd;) && python3 main.py";} | crontab -u $(logname) -

apt install ffmpeg