import requests  
import time  
print("RADAR PRO - WITH CACHE")  
print("=====================")  
cache_data = None  
cache_time = 0  
def get_aircraft():  
    global cache_data, cache_time  
