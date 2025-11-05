@echo off 
title DRONE DEFENSE CONTROL CENTER 
cd /d %%~dp0 
 
:MENU 
cls 
echo ======================================== 
echo     DRONE DEFENSE CONTROL CENTER 
echo ======================================== 
echo. 
echo [1] LAUNCH WEB DASHBOARD 
echo [2] START MOTION DETECTION 
echo [3] START AIRCRAFT RADAR 
echo [4] START DRONE DETECTOR 
echo [5] SYSTEM INFORMATION 
echo [6] INSTALL PYTHON LIBS 
echo [7] EXIT 
echo. 
set /p choice="SELECT OPTION: " 
 
if "%choice%"=="1" goto DASHBOARD 
if "%choice%"=="2" goto MOTION 
if "%choice%"=="3" goto RADAR 
if "%choice%"=="4" goto DRONE 
if "%choice%"=="5" goto INFO 
if "%choice%"=="6" goto INSTALL 
if "%choice%"=="7" exit 
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
echo SYSTEM INFORMATION 
echo ======================================== 
echo Location: C:\DroneDefense 
echo. 
dir 
echo. 
pause 
goto MENU 
 
:INSTALL 
echo Installing Python libraries... 
pip install opencv-python requests numpy 
pause 
goto MENU 
