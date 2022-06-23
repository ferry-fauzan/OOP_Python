class Hero:

    def __init__(self,name,power):
        self.name=name
        self.power=power 

class Hero_Intelligent(Hero):
    pass

class Hero_Strength(Hero):
    pass

raka=Hero("Raka",200)
techis=Hero_Intelligent('techis',50)
rock=Hero_Strength('Rock',500)


print(raka.name)
print(techis.power)
print(rock.name)