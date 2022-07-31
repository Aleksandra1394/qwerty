def deco(some_func):
    def wrapper():
        print("wrapper after")
        some_func()
        print("wrapper before")
        return some_func
    return wrapper