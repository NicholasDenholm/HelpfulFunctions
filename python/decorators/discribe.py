import inspect

def deep_describe(func):
    def wrapper(obj, *args, **kwargs):
        print("Class:", obj.__class__.__name__)
        print("Module:", obj.__class__.__module__)
        print("Bases:", [b.__name__ for b in obj.__class__.__bases__])
        print("Attributes:")
        for name, val in obj.__dict__.items():
            print("  ", name, "=", val)
        print("Methods:")
        for name, meth in inspect.getmembers(obj, predicate=inspect.ismethod):
            print("  ", name)
        return func(obj, *args, **kwargs)
    return wrapper
