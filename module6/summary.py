class Book:
    def __init__(self,name) -> None:
        self.name = name

    def read(self):
        raise NotImplementedError #NotImplementedError jor kore implement kora hoy. abstract class a eta implement kora hoye thake.


class Physics(Book):
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name)

    def read(self):
        print('reading physics vector chapter')

topon = Physics('topon',True)

print(issubclass(Physics,Book)) #'physics' class  'Book' er subclass kina check korbe issubclass()

print(isinstance(topon,Physics))# 'topon' object 'Physics' class er instance kina, orthat 'topon' object 'Physics' class theke create hoyese kina ta check korbe isinstance

print(isinstance(topon,Book))

topon.read()# read() child class 'Physics' a first read()  method ke khujbe. jodi 'Physics' class read method ke peye jae tobe print kore dibe. ta na hole 'Physics' er parent class 'Book' class a read() method ke khujbe