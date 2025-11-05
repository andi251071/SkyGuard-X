@echo off 
:loop 
python radar_distance.py 
python performance_check.py 
timeout 10 
goto loop
