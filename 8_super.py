class Hero:

    def __init__(self,name,power):
        self.name=name
        self.power=power 
    def showInfo(self):
        print("{} dengan health: {}".format(self.name,self.power))

# class Hero_intel(Hero):
#     def __init__(self,name):
#         super().__init__(name,200)
#         super().showInfo()
    


# lina=Hero_intel('lina')
raka=Hero("Raka",200)
print(raka.name)
# print(f'{lina.name} & {lina.power}')