from unicodedata import name


class Hero:
    def __init__(self, nama, health,power):
        self.__name=nama
        self.__health=health
        self.__power=power

    #getter
    def getName(self):
        return self.__name
    def gethealth(self):
        return self.__health


    #setter
    def tusuk(self,powerLawan):
        self.__health -= powerLawan    

#awal game
jumanji=Hero('Juma', 50,500)

print(jumanji.__dict__)
print(f"Hero pertama bernama  {jumanji.getName()}")
jumanji.tusuk(20)
print(jumanji.gethealth())