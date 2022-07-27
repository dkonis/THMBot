@echo off

echo [91m88888888888 888    888 888b     d888 888888b.            888    
echo     888     888    888 8888b   d8888 888  "88b           888    
echo     888     888    888 88888b.d88888 888  .88P           888    
echo     888     8888888888 888Y88888P888 8888888K.   .d88b.  888888 
echo     888     888    888 888 Y888P 888 888  "Y88b d88""88b 888    
echo     888     888    888 888  Y8P  888 888    888 888  888 888    
echo     888     888    888 888   "   888 888   d88P Y88..88P Y88b.  
echo     888     888    888 888       888 8888888P"   "Y88P"   "Y888 [0m

echo:
SCHTASKS /DELETE /TN "THMBot"
del THMBot.xml
del account.conf