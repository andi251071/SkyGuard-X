import pandas as pd 
from sklearn.ensemble import RandomForestClassifier 
import joblib 
import sqlite3 
import numpy as np 
 
conn = sqlite3.connect('drones.db') 
cursor = conn.cursor() 
 
try: 
    df = pd.read_sql_query('SELECT * FROM sensor_data', conn) 
    if len(df) 
        print('Training AI model with real data...') 
        features = ['battery_level', 'vibration', 'temperature'] 
        X = df[features].fillna(0) 
        y = df['maintenance_flag'] 
        model = RandomForestClassifier(n_estimators=10) 
        model.fit(X, y) 
        joblib.dump(model, 'predictive_maintenance_model.pkl') 
        print('AI Model trained with real data!') 
    else: 
        raise Exception('Not enough data') 
except: 
    print('Creating demo AI model...') 
    demo_data = pd.DataFrame({ 
        'battery_level': np.random.randint(10, 100, 100), 
        'vibration': np.random.uniform(1, 10, 100), 
        'temperature': np.random.randint(20, 40, 100) 
    }) 
    features = ['battery_level', 'vibration', 'temperature'] 
    model = RandomForestClassifier(n_estimators=10) 
    model.fit(demo_data[features], demo_data['maintenance_flag']) 
    joblib.dump(model, 'predictive_maintenance_model.pkl') 
    print('Demo AI Model created!') 
 
conn.close() 
print('AI setup completed!') 
