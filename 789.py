def my_func(a):
    l1=[]
    print(a)
    for i in a:
        l1.append(i*3)
        print(l1)

    return l1

l = [1,2,3]
print(l)
l.append(4)
print(l)
l.append(5)
print(l)
b = my_func(l)
print(b)
