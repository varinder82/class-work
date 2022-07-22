# single inheritance
class A():
    def func1(self):
        print("a")
class B(A):
        def func2(self):
            print("b")
ob = B()
ob.func1()
ob.func2()
# multilevel inheritance
class a:
    def f1(self):
        print("A")


class b(a):
    def f2(self):
        print("B")


class c(b):
    def f3(self):
        print("C")


ob = c()
ob.f1()
ob.f2()
ob.f3()
# multiple inheritance
class a:
    def f1(self):
        print("K")


class b():
    def f2(self):
        print("L")


class c(a, b):
    def f3(self):
        print("M")


ob = c()
ob.f1()
ob.f2()
ob.f3()
# hierarichal inheritance
class a:
    def f1(self):
        print("A")


class b(a):
    def f2(self):
        print("B")


class c(a):
    def f3(self):
        print("C")


ob1 = c()
ob2 = b()
ob1.f1()
ob2.f2()
ob1.f3()
# hybrid inheritance
class a:
    def f1(self):
        print("A")


class b(a):
    def f2(self):
        print("B")


class c(a):
    def f3(self):
        print("C")


class d(b, c):
    def f4(self):
        print("D")


ob1 = d()
ob1.f1()
ob1.f2()
ob1.f3()
ob1.f4()
