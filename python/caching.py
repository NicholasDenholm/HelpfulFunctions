def caching(f):
    cache = {}
    def cacheing_version_of_f(*args):
        if args in cache: 
            print(f"[CACHE HIT] {f.__name__}{args} -> {cache[args]}")
            return cache[args]
        print(f"[CACHE MISS] {f.__name__}{args}")
        result = f(*args)
        cache[args] = result
        return result
    return cacheing_version_of_f

@caching
def add(x, y): 
    return x + y

@caching
def sub(x,y):
    return x - y

#add(4,5)
#add(4,5)

#sub(4,5)

#sub(4,7)
#sub(4,7)