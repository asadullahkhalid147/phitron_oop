# static attribute (class attribute)
# staticmethod -> @staticmethod
# classmethod -> @classmethod
# defference between static method and class method

class Shopping:
    cart = [] #static or class attribute
    origin = 'china'

    def __init__(self,name,location) -> None:
        self.name = 'jamuna' #instance attribute
        self.location = 'bashundhara'

    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying: {item} for: {price} and remaining: {remaining}')


    @staticmethod # static method a class.method(parameer_of_method)  diye call korte parbo. tasara method create korar shomoy 'self' lekhar dorkar nai
    def multiply(a,b):
        result= a*b
        print(result)

    @classmethod #class method use korle amar object use kora lagbe na. direct class.method(parameter_of_method) diye call korte parbo
    def hudai_dekhi(self,item):
        print('hudai dekhi kintu kinmu na. just ac er hawa khai',item)

bashundhara = Shopping('bashu en dhara', 'not popular location')
# bashundhara.purchase('lungi',500,1000)
# Shopping.purchase('a',2,3,3)

bashundhara.hudai_dekhi('lungi')
Shopping.hudai_dekhi('lungi')

Shopping.multiply(4,6)
bashundhara.multiply(6,9)#evabe object diye call kora uchit na static mehtod er belae