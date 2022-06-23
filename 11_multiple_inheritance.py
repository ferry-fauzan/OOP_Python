from unicodedata import name


class A:
    def method_A(self):
        print('Ini adalah method A')
class B:
    def method_B(self):
        print('ini adalah method B')

class sesuatu(A,B): #multiple inheritance
    pass

objek=sesuatu()

objek.method_A() #bisa akses a
objek.method_B() #bisa akses b


class tim:
    def setTim(self,nameTim):
        self.tim=nameTim 
    def showTeam(self):
        print(self.tim)

class pos:
    def setPos(self,position):
        self.position=post
    def showPos(self):
        print(self.post)

class player(tim,pos):
    def __init__(self,name):
        self.name=name

    def showPlayer(self):
        print("My name is", self.name)

        # print("My name {} \nMy Position {}".format(
        #     self.team,
        #     self.post
        # ))

ojan=player('Ojan')
ojan.showPlayer()
ojan.setTim('Chelsea')

ojan.showTeam()


