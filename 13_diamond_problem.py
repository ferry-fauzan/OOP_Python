class A:
    def show(self):
        print("Ini adalah show A")
class B(A):
    def show(seLf):
        print("Ini adalah show B")
class C(B):
    def show(self):
        print("Ini adalah show C")

class D(B,C):
    pass

objek=D()
objek.show()
help(objek)