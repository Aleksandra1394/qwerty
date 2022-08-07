class j:
    arg = "Alice"

    def my_method(self, name):
        print("Hello, ", name)


class y:
    arg = "Alice"

    def __init__(self, name, surname):
        self.name = name

    def my_method(self):
        print("Hello, ", self.name)

class b:
        arg = "Alice"

        def __init__(self, name, surname):
                self.name = name

        def __my_private_method(self):
            print("just private")

        def my_method(self):
            print("Hello, ", self.name)

            class A1:
                def __init__(self):
                    self.n = 10

                def total(self, a):
                    return self.n + int(a)

            class A2:
                def __init__(self):
                    self.string = 'Hi'

                def total(self, a):
                    return len(self.string + str(a))

            a1 = A1()
            a2 = A2()

            print(a1.total(35))
            print(a2.total(35))


class A1:
    def __init__(self):
        self.n = 10

    def total_a1(self, a):
        return self.n + int(a)


class A2:
    def __init__(self):
        self.n = 15

    def total_a2(self, a):
        return self.n + int(a)


class A3(A1, A2):

    def total_a3(self, a):
        return self.n + int(a)


a2 = A3()
print(a2.n)
print(a2.total_a3(1))
