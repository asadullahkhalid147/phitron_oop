class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('val mangso polau korma')

    def exercise(self):
        raise NotImplementedError #raise NotImplementedError diye over ride kortei hbe,eta bujae.orthat object 'sakib' jokhon exercise ke call korbe tokhon 'child' class ao ekta 'exercise' method thakte hbe je parent class er 'exercise' method ke override korbe 



class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    # parent class a je eat() method ta ase take child class er eat() method ta override kore felse

    # override
    def eat(self):
        print('vegetables')

    def exercise(self):
        print('gym a poisa diye gham jhorai')

    # dandaar or magic method. this is special method. overloading 
    def __add__(self,other):
        return self.age + other.age # duita cricketer object ke jog(+) kori. tahole 1st cricketer er age and second cricketer er age jog kore dibe.

    def __mul__(self,other):
        return self.weight * other.weight
    
    def __len__(self):
        return self.height

sakib = Cricketer('sakib',38,68,91,'BD')
mushi = Cricketer('mushi',36,65,78,'BD')
sakib.eat()
sakib.exercise()

# (+)plus sign overload kortesi
print(45+63)
print('Sakib'+'Rakib')
print([12,98]+[5,6,7,1,2])

print(sakib+mushi)
print(sakib*mushi)
print(len(sakib))