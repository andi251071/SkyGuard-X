@echo off 
echo ?? SETUP ENHANCED DRONE SYSTEM 
python -m venv skyport_env 
call skyport_env\Scripts\activate 
pip install flask pandas scikit-learn joblib 
echo ? Environment setup complete! 
pause 
