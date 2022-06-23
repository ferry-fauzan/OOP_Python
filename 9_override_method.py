class Hero:
    def __init__(self,name, health):
        self.name=name
        self.health=health

    def showInfo(self):
        print('Show Info di class Hero')
        print("{} health level: {}".format(self.name,self.health))

class HeroIntel(Hero):
    def __init__(self,name):
        super().__init__(name,100)

    def showInfo(self):
        print('Show Info di class Hero Intelligent')
        print("{} \n \t Tipe: Intelligent \n Health: {}".format
        (
            self.name,
            self.health
        ) )

class HeroStrength(Hero):
    def __init__(self,name):
        super().__init__(name,400)
        

lina=HeroIntel('lina')
axe=HeroStrength('axe')

lina.showInfo()
axe.showInfo()