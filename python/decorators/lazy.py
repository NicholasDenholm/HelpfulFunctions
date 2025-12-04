def partial_eval(*original_args, **original_kwargs):
    def decorator(f):
        def partial_eval_of_f(*args, **kwargs):
            new_args = original_args + args
            new_kwargs = dict(original_kwargs)
            new_kwargs.update(kwargs)
            return f(*new_args, **new_kwargs)
        return partial_eval_of_f
    return decorator


@partial_eval(2)
def mult(x,y):
    return x * y

print(mult(5))


@partial_eval(y=3)
def div(x,y):
    return x / y

print(div(5))