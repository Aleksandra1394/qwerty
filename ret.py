a = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
#for i in a:
    #if i < 5:
        #print(i)



my_list=["a","c","d"]
#for i in my_list:

  #  print(i)

my_dict={"r":1,}
#for k, v in my_dict.items():
#    print(k,v)


l1 = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
l2 = [1, 2, 1, 2, 101, 7, 43, 9, 10, -1, 0]


def my_funk(a, b):
    print(a,b )

    for i in a:
        print("=======================")
        print(i)
        print("=======================")
        for c in b:
            if c == i:
                a.remove(i)
                print("WWWWWWWW")
                print(a)
                print(i, c)
                print("WWWW")
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
    return a

print("!!!!!!!!!!!!!!!!!!!!!!!!")
d= my_funk(l1, l2)
print(d)





my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
for k, v in my_dict.items():
   print(k,v)










