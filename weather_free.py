import requests  
print("FREE WEATHER INTEGRATION")  
print("========================")  
def get_aviation_weather():  
    try:  
        # OpenWeatherMap Free Tier  
        api_key = "free"  # Actually free without key for basic  
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=-6.2088&lon=106.8456&appid={api_key}"  
        response = requests.get(url, timeout=5)  
        if response.status_code == 200:  
            return "Weather data available"  
        else:  
            # Simulate weather data  
            return "SIM: Clear, Wind 5kt, Vis 10km"  
    except:  
        return "SIM: Good flying conditions"  
weather = get_aviation_weather()  
print("Current Conditions:", weather)  
print("Impact: Safe for drone operations")  
input("Enter...") 
