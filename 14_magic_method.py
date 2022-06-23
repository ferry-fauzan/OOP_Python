class Mangga:
    def __init__(self,nama,berat):
        self.nama=nama
        self.berat=berat
    
    def __repr__(self):
        return "Debug-Mangga : {}".format(self.nama)

    def __str__(self):
        return "Mangga : {}".format(self.nama)

    def __add__(self,objek):
        return self.berat+objek.berat
    
arummanis=Mangga("Arum Manis", 100)
kweni=Mangga("Kweni", 77)
print(arummanis)
print(repr(kweni))
print(arummanis+kweni)

