# read only-->you can not set the value. value can not be changed
#getter--> get  a value of a property through a method. Most of the time, you will get the value of a private attribute
#setter--> set a value of a property through a method. most of the time you will set the value of a private property.
class User:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    @property#'@property' kono function er upor lekha thakle shetake decorator bole.er fole 'age' function ta attribute hoye gese. eta ekhon ar method er moto kaj korbe na

    #"getter" without any setter is readonly attribute
    # getter mane kono ekta man ke get korbo

    def age(self):
        return self._age#1st method: setting value from outside in private property 'age'
    @property
    def salary(self):
        return self.__money
    
    # setter mane kono ekta man ke set korbo
    #setter
    @salary.setter
    def salary(self,value):
        if value<0:
            return 'salary cannot be negative'
        self.__money +=value

samsu = User('Kopa',21,12000)
# print(samsu.__money)

# print(samsu.age())
print(samsu.age)#calling 'age' method like as "attribute" because "@property" "age" method er upor use korae age method attribute er moto kaj korese

# print(samsu.salary())
print(samsu.salary)

samsu.salary=4500 #setter er karone salary te aro 4500 taka jog hbe
print(samsu.salary)