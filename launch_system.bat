@echo off 
echo MEMULAI DRONE DEFENSE SYSTEM... 
 
echo 1. Starting Radar System... 
start python radar_distance.py 
 
echo 2. Starting Drone Controller... 
start python drone.py 
 
echo 3. Starting Alert System... 
start python alert_system.py 
 
echo 4. Starting Web Server... 
start python server.py 
 
echo 5. Opening Dashboard... 
timeout 3 
start dashboard.html 
 
echo SYSTEM READY! 
pause
