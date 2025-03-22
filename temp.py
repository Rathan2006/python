import time
import functools

def rate_limit(max_calls, period):
    calls = []
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            now = time.time()
            # Remove calls that are older than the period
            calls = [call for call in calls if now - call < period]
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=5)
def api_request():
    return "API response"
api_request() 
api_request() 
api_request() 


