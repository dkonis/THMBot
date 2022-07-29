#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'

echo -e "${RED} 88888888888 888    888 888b     d888 888888b.            888"
echo -e "     888     888    888 8888b   d8888 888  \"88b           888"
echo -e "     888     888    888 88888b.d88888 888  .88P           888"
echo -e "     888     8888888888 888Y88888P888 8888888K.   .d88b.  888888"
echo -e "     888     888    888 888 Y888P 888 888  \"Y88b d88\"\"88b 888"
echo -e "     888     888    888 888  Y8P  888 888    888 888  888 888"
echo -e "     888     888    888 888   \"   888 888   d88P Y88..88P Y88b."
echo -e "     888     888    888 888       888 8888888P\"   \"Y88P\"   \"Y888${NC}"

read -p "Are you sure you want to uninstall THMBot (Y/N): " ANS

if  [ "$ANS" = "Y" ] || [ "$ANS" = "y" ]
then
    crontab -l | grep -v '&& python3 main.py'  | crontab -
    rm account.conf
    rm tryhackmebot.log
    rm -rf __pycache__
    rm -rf .wdm
    rm -rf recapchasound
fi