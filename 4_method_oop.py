class Hero:
    #class variable
    jumlah_hero=0

    def __init__(self,input_name,inputHealth,inputPower):
        #instance varoiable
        self.name=input_name
        self.health=inputHealth
        self.power=inputPower
        Hero.jumlah_hero += 1

    #void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(f'Namaku adalah {self.name}')
    
    #method dengan argumen, tanpa return
    def powerUp(self,up):
        self.power += up
        # print(f'Power {self.name} bertambah {up} menjadi {self.power}')
    
    #method dengan return
    def getPower(self):
        return self.power

heroA=Hero('Mage',5,500)
heroB=Hero('Tank',2,800)

heroA.siapa()
heroB.powerUp(30)
print(heroB.getPower())