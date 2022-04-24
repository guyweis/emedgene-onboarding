import functools


def main():
    print(recur_fibo(6))
    print(recur_fibo(8))


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return getattr(func, str(*args))
        except AttributeError:
            value = func(*args, **kwargs)
            setattr(func, str(*args), value)
            return value
    return wrapper


@my_decorator
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))












# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


