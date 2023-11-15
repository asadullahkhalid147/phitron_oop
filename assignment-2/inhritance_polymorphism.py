class Animal:
    def __init__(self,name) -> None:
        self.name = name
     
    def make_sound(self):
        print('animal making some sound')


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)


    def make_sound(self):
        print('meow')


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)


    def make_sound(self):
        print('gheu gheu')




class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)


    def make_sound(self):
        print('beh beh')


   
don = Cat('Real don')
shepard = Dog('Local shepard')
mess = Goat('chagol')


for animal in (don,shepard,mess):
    print(animal.name)
    animal.make_sound()
