import time 
 
class HighPerformanceCache: 
    def __init__(self): 
        self.cache = {} 
        self.stats = {"hits": 0, "misses": 0} 
 
    def get(self, key): 
        if key in self.cache: 
            data, expiry = self.cache[key] 
            data, expiry = self.cache[key] 
                self.stats["hits"] += 1 
                return data 
        self.stats["misses"] += 1 
        return None 
 
    def set(self, key, value, ttl=300): 
        expiry = time.time() + ttl 
        self.cache[key] = (value, expiry) 
        return True 
        return True 
 
    def get_stats(self): 
        total = self.stats["hits"] + self.stats["misses"] 
        hit_rate = self.stats["hits"] / total * 100 if total > 0 else 0 
        return {"hit_rate": f"{hit_rate:.1f}%"} 
def cache_response(ttl=300): 
    def decorator(f): 
        def decorated_function(*args, **kwargs): 
            cache_key = f"{f.__name__}" 
            cache = HighPerformanceCache() 
            cached = cache.get(cache_key) 
            if cached: 
                return cached 
            result = f(*args, **kwargs) 
            cache.set(cache_key, result, ttl) 
            return result 
        return decorated_function 
    return decorator 
