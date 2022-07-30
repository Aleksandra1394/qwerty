def my_func(a):
    print(a)
    b=my_func(2)
    b=my_func(a)


def my_func2(a=1):
    print(a)


def my_func4(*args):
    print(args)

my_func4(1,2,3)

my_func4(1,2,3,5,6,7,7,8)

my_func4("asd")

def my_func5(**kwargs):
    print(kwargs)
my_func5(a=1,b=5)

def my_func6(*args, **kwargs):
    print(args,kwargs)
my_func6(1, 2, 3, 'abc', a=1, b=2, c=3)




