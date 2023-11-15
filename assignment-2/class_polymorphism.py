class Car:
    def __init__(self,name,value) -> None:
        self.name = name
        self.value = value


    def run(self):
        print("drive")




class Cycle:
    def __init__(self,name,value) -> None:
        self.name = name
        self.value = value


    def run(self):
        print("move")


class Ship:
    def __init__(self,name,value) -> None:
        self.name = name
        self.value = value


    def run(self):
        print("sail")


car= Car("marcedes","20000")
cycle = Cycle("joyita","200")
ship = Ship("Agun71","45000")


for x in (car,cycle,ship):
    x.run()