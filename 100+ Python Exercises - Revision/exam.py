import datetime as dt
def my_decor(fun):
    def wrapper():
        t1 = dt.datetime.now()
        fun()
        t2 = dt.datetime.now()
        print(t2-t1)
    return wrapper

@my_decor
def my_func():
    print('Something')

my_func()
