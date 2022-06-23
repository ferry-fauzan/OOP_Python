#membuat class abstract
# abc=abstract based class

from abc import ABC,abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass

class PushButton(Button):
    def click(self):
        print("push button clicks")

class RadioButton(Button):
    def click(self):
        print("push radio click ")

tombol1=PushButton()
tombol2=RadioButton()



tombol1.click()
tombol2.click()