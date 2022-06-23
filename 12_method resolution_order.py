class A:
    def show(self):
        print("Ini adalah Show A")

class B:
    def show(self):
        print("Ini adalah show B")


class C(A,B):
    pass

objek=C()
objek.show()
