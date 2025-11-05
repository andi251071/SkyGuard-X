@echo off 
title ?? DRONE DEFENSE CONTROL CENTER 
cd /d %%~dp0 
 
:MENU 
cls 
echo ======================================== 
echo    DRONE DEFENSE CONTROL CENTER 
echo ======================================== 
echo. 
echo [1] ?? LAUNCH WEB DASHBOARD 
echo [2] ?? START MOTION DETECTION 
echo [3] ??? START AIRCRAFT RADAR 
echo [4] ?? START DRONE DETECTOR 
echo [5] ?? SYSTEM INFORMATION 
echo [6] ?? INSTALL PYTHON LIBS 
echo [7] ? EXIT 
echo. 
set /p choice="SELECT OPTION: " 
 
if "%%choice%%"=="1" goto DASHBOARD 
if "%%choice%%"=="2" goto MOTION 
if "%%choice%%"=="3" goto RADAR 
if "%%choice%%"=="4" goto DRONE 
if "%%choice%%"=="5" goto INFO 
if "%%choice%%"=="6" goto INSTALL 
if "%%choice%%"=="7" exit 
goto MENU 
 
:DASHBOARD 
echo Launching Web Dashboard... 
start dashboard.html 
timeout /t 2 
goto MENU 
 
:MOTION 
echo Starting Motion Detection... 
python motion.py 
goto MENU 
 
:RADAR 
echo Starting Aircraft Radar... 
python radar.py 
goto MENU 
 
:DRONE 
echo Starting Drone Detection... 
python drone.py 
goto MENU 
 
:INFO 
cls 
echo ?? DRONE DEFENSE SYSTEM INFO 
echo ======================================== 
echo Location: C:\DroneDefense 
echo. 
echo ?? FILES: 
echo  control.bat - Main Control Center 
echo  dashboard.html - Web Dashboard 
echo  motion.py - Motion Detection 
echo  radar.py - Aircraft Radar 
echo  drone.py - Drone Detector 
echo. 
echo ?? REQUIREMENTS: 
echo  Python 3.x 
echo  Webcam (for motion detection) 
echo  Internet (for aircraft radar) 
echo. 
pause 
goto MENU 
 
:INSTALL 
echo Installing Python libraries... 
pip install opencv-python requests numpy 
echo. 
echo ? Libraries installed! 
pause 
goto MENU 
