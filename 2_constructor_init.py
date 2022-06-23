class Hero: #template
    def __init__(self,input_name,input_power,input_armor):
        self.name=input_name
        self.power=input_power
        self.armor=input_armor

hero1=Hero('wardhani',20,500)
hero2=Hero('saradha',60,500)

print(hero1)
print(hero1.__dict__)
print(hero2.power)


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