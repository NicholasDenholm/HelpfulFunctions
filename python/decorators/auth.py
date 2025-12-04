def requires_admin(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if user != "admin":
            raise PermissionError("Admin privileges required")
        return func(*args, **kwargs)
    return wrapper


@requires_admin
def add(x,y):
    return x + y


add(1,1)