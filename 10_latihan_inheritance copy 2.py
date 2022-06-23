class Hero:
    def __init__(self,name):
        self.__name=name
        self.health_pool=[10,20.30,40,50,90]
        self.attPower_pool=[5,10,15,20]
        self.armor_pool=[0,1,2,3,4,5]
        self.__exp=0
        self.__level=0

    def show_info(self):
        print("{} \n\tLevel: {}\n\thealth:{} \n\tattPower:{} \n\tarmor:{} ".format(
        self.__name,
        self.__level,
        self.__health,
        self.__attPower,
        self.__armor
        )
        )

    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool=input

    @attPower_pool.setter
    def attPower_pool(self,input):
        self.__attPower_pool=input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool=input

    @gainExp.setter
    def gainExp(self,input):
        self.__exp+=input
        if(self.__exp>=100):
            self.levelUp=self.__exp//100
            self.__exp%=100

    @levelUp.setter
    def levelUp(self,input):
        self.__level+=input
        self.__health=self.__health_pool[self.__level]
        self.__attPower=self.__attPower_pool[self.__level]
        self.__armor=self.__armor_pool[self.__level]

class HeroIntelligent(Hero):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool=[0,50,100,150,200,250]
        self.attPower_pool=[0,20,40,60,80,100]
        self.armor_pool=[0,0.5,1,1.5,2]
        self.levelUp=1

class HeroStrength(Hero):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool=[0,200,300,400,500,600]
        self.attPower_pool=[0,20,40,60,80,100]
        self.armor_pool=[0,0.5,1,1.5,2]
        self.levelUp=1

lina=HeroIntelligent('lina')
lazar=HeroStrength('lazar')

lina.show_info()
lazar.show_info()