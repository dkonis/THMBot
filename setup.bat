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
set /p MAIL="Set Your THM Email: "
set /p PASS="Set Your THM Password: "  

echo [account] > account.conf
echo mail = %MAIL% >> account.conf
echo PASS = %PASS% >> account.conf

echo:
echo [93mNote: to update your account credentials change - [100m[37m account.conf [0m[0m[0m 

echo ^<?xml version="1.0" encoding="UTF-16"?^> > THMBot.xml
echo ^<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"^> >> THMBot.xml
echo   ^<Triggers^> >> THMBot.xml
echo     ^<CalendarTrigger^> >> THMBot.xml
echo       ^<StartBoundary^>%date:~6,4%-%date:~3,2%-%date:~0,2%T04:00:00^</StartBoundary^> >> THMBot.xml
echo       ^<Enabled^>true^</Enabled^> >> THMBot.xml
echo       ^<ScheduleByDay^> >> THMBot.xml
echo         ^<DaysInterval^>1^</DaysInterval^> >> THMBot.xml
echo       ^</ScheduleByDay^> >> THMBot.xml
echo     ^</CalendarTrigger^> >> THMBot.xml
echo   ^</Triggers^> >> THMBot.xml
echo   ^<Principals^> >> THMBot.xml
echo     ^<Principal id="Author"^> >> THMBot.xml
echo       ^<LogonType^>Password^</LogonType^> >> THMBot.xml
echo       ^<RunLevel^>LeastPrivilege^</RunLevel^> >> THMBot.xml
echo     ^</Principal^> >> THMBot.xml
echo   ^</Principals^> >> THMBot.xml
echo   ^<Settings^> >> THMBot.xml
echo     ^<MultipleInstancesPolicy^>IgnoreNew^</MultipleInstancesPolicy^> >> THMBot.xml
echo     ^<DisallowStartIfOnBatteries^>true^</DisallowStartIfOnBatteries^> >> THMBot.xml
echo     ^<StopIfGoingOnBatteries^>true^</StopIfGoingOnBatteries^> >> THMBot.xml
echo     ^<AllowHardTerminate^>true^</AllowHardTerminate^> >> THMBot.xml
echo     ^<StartWhenAvailable^>false^</StartWhenAvailable^> >> THMBot.xml
echo     ^<RunOnlyIfNetworkAvailable^>false^</RunOnlyIfNetworkAvailable^> >> THMBot.xml
echo     ^<IdleSettings^> >> THMBot.xml
echo       ^<StopOnIdleEnd^>false^</StopOnIdleEnd^> >> THMBot.xml
echo       ^<RestartOnIdle^>false^</RestartOnIdle^> >> THMBot.xml
echo     ^</IdleSettings^> >> THMBot.xml
echo     ^<AllowStartOnDemand^>true^</AllowStartOnDemand^> >> THMBot.xml
echo     ^<Enabled^>true^</Enabled^> >> THMBot.xml
echo     ^<Hidden^>false^</Hidden^> >> THMBot.xml
echo     ^<RunOnlyIfIdle^>false^</RunOnlyIfIdle^> >> THMBot.xml
echo     ^<WakeToRun^>false^</WakeToRun^> >> THMBot.xml
echo     ^<ExecutionTimeLimit^>PT72H^</ExecutionTimeLimit^> >> THMBot.xml
echo     ^<Priority^>5^</Priority^> >> THMBot.xml
echo   ^</Settings^> >> THMBot.xml
echo   ^<Actions Context="Author"^> >> THMBot.xml
echo     ^<Exec^> >> THMBot.xml
echo       ^<Command^>%cd%%\main.py^</Command^> >> THMBot.xml
echo       ^<WorkingDirectory^>%cd%%^</WorkingDirectory^> >> THMBot.xml
echo     ^</Exec^> >> THMBot.xml
echo   ^</Actions^> >> THMBot.xml
echo ^</Task^> >> THMBot.xml

echo:
SCHTASKS /CREATE /TN "THMBot" /RU %username% /XML THMBot.xml