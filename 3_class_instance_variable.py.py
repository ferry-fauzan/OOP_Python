class Hero: #template
    #class vairable/static variable
    jumlah=0


    def __init__(self,input_name,input_power,input_armor): #instance vaiable
        self.name=input_name
        self.power=input_power
        self.armor=input_armor
        Hero.jumlah+=1
        print(f'Nama hero {self.name}')

hero1=Hero('wardhani',20,500)
print(Hero.jumlah)
hero2=Hero('saradha',60,500)
print(Hero.jumlah)

 
# print(hero1.name)
# print(Hero.jumlah)
# print(hero2.__dict__)
# print(Hero.jumlah)
# print(hero2.power)








# hero1=Hero()    #object/instance
# hero2=Hero()
# hero3=Hero()

# hero1.name='sinper'
# hero2.health=100

# hero2.name='sven'
# hero2.health=200

# hero3.name='otong'
# hero3.health=400


# print(hero1)
# print(hero1.__dict__)

# print(hero1.name)