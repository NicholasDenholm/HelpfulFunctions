
def logging(f):
    def logging_of_f(*args, **kwargs):
        print(f"[CALL] {f.__name__}{args}{kwargs if kwargs else ""}")
        result = f(*args, **kwargs)
        print(f"[RETURN] {f.__name__} --> {result} ")
        return result
    return logging_of_f

@logging
def add(x,y):
    return x + y
        
add(1,1)

