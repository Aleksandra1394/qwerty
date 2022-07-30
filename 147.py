def my_func(a):
    l1 = []
    for i in a:
        l1.append(i*5)
    print(l1)
    return l1


l2=[4,5,6]
print(l2)
b=my_func(l2)
print(b)