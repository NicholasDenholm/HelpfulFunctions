import time
from caching import caching

def runtime(f):
    def runtime_of_f(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() 
        print(f"[TIME] {f.__name__}{args} took: {end_time - start_time:.6f} seconds")
        return result
    return runtime_of_f

@runtime
@caching
def add(x,y):
    time.sleep(0.2)
    return(x + y)

print(add(1,2))
print(add(1,2))


print(add(2,2))
print(add(1,2))