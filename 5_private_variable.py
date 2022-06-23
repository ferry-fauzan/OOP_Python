class Hero:
    #class variable
    jumlah=0
    __privateJunlah=0 # privat
    def __init__(self, name, health):
        self.name=name
        self.health=health
        self.__private='private' #privat


lina=Hero('lina', 200)
# print(lina.private)
print(lina.__dict__)
lina.__private='Aku Privat'
print(lina.__private)