import time

def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retry {i+1}/{times}: {e}")
                    time.sleep(0.2)
            raise Exception("Function failed after retries")
        return wrapper
    return decorator



@retry(5)
def add(x,y):
    return x + y


print(add(1,"a"))