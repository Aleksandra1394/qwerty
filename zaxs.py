import time
def deco(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(" wrapper after ")
        func(*args, **kwargs)
        end_time=time.time()
        res_time=end_time-start_time
        print("время выполнения.")
        print(res_time)
        return func
    return wrapper


@deco




def my_func(a,b):
    print(a+b)


@deco
def my_name(s):
    time.sleep(5)
    print(s)



my_func(3,4)
my_name({"aqsw":"defr"})

t= time.time()
print(t)














