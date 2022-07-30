
def my_func(a):
    print(a)
    for i in a:
        print(i*3)


l = [1,2,3]
print(l)
l.append(4)
print(l)
l.append(5)
print(l)
b = my_func(l)
print(b)
