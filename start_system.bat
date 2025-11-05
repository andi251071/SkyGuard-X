@echo off
title Drone Defense System
echo Starting Drone Defense System...
echo.
start python radar_simple.py
timeout 1
start python motion_simple.py  
timeout 1
start python alert_simple.py
timeout 1
echo.
echo Starting Web Dashboard...
python orchestrator_simple.py
