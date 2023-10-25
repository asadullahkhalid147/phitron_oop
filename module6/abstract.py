from abc import ABC, abstractmethod
# abc = abstract base class 
class Animal(ABC):
    @abstractmethod #enforce all derived class to have a 'eat' method
    def eat(self):
        print('i need food')

    @abstractmethod
    def move(self):
        print('Hanging on the branches')

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.catagory='Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('khabo kola')

    def move(self):
        print('gase lafae')


layka = Monkey('lucky')
layka.eat()