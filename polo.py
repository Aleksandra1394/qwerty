my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
def max_key_in_dict(a):
    keys = []
    for i in a:
         if a[i] is not None:
            keys.append(max_key_in_dict(a[i]))
    else:
        keys.append(i)
        return max(keys)




import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

@time_of_function
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


print(func("1", "0"))





