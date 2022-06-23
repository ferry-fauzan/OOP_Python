class Hero: #template
    pass

hero1=Hero()    #object/instance
hero2=Hero()

hero1.name='sinper'
hero2.health=100

hero2.name='sven'
hero2.health=200

hero2.name='otong'
hero2.health=400


print(hero1)
print(hero1.__dict__)

print(hero1.name)