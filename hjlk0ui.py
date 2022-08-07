class A:
    arg = 1
    def __init__(self, name):
        print(name)

    def my_method(self,a):
        print(a)
    def my_secondmethod(self,c):
        print(c)
a=A("2")
b=A("d458")
a.my_method("Привет")
b.my_method("Как дела?")

a.my_secondmethod(1234567890)
b.my_secondmethod("Asdewq")

print(a.arg)
print(b.arg)
