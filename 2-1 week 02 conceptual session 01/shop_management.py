class Product:
    def __init__(self,name,price,quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity



class Store:
    def __init__(self) -> None:
        
        self.__products_price={} #dictionary-->product er price ase {key:value}=={product_name:product_price} key=product value= product_price
        self.__products_quantity = {} #dictionary-->product er quantity ase
        # {key:value}=={product_name:product_quantity}
        self.__profit=0

    
    def add_product(self,name,price,quantity):

        product = Product(name,price,quantity)
        
        self.__products_price[product.product_name]=product.product_price#self.product_price['iphone']=200000. this is the example given below of "pd" object
        self.__products_quantity[product.product_name]=product.product_quantity #self.product_quantity ['iphone']=10

    
    def buy_product(self,name,quantity):
        if name in self.__products_price:#product_price er vitor product ase kina khoja hosse
            if self.__products_quantity[name] >=quantity:#product_quantity er theke  customer er quantity beshi ba kom kina check kora hosse 
                #profit calculate korsi
                self.__profit = self.__profit + ((5*self.__products_price[name])/100)*quantity
                #deduct product quantity
                self.__products_quantity[name]= self.__products_quantity[name]-quantity#mul product theke customer er product bad deoya hosse
                print("Thank YOU")
            else:
                print("Unavailable")
        else:
            print("Not Found")




    def show_products(self): 
        print("all products price: ",self.__products_price)
        print("all product quantity: ",self.__products_quantity)

    def show_profit(self):
        print("profit: ",self.__profit)#private property profit ke show koranor jonno ekta method banassi

class Shop(Store):
    def __init__(self,name) -> None:
        self.shop_name = name
        super().__init__() #shop class store class ke inherit korese.ekane "super" "Store" class er constructor ke call korse. call korar time a "super().__init__()" tar __init__()bracket er vitore parameter hishebe kisu nae nai, karon "Store()"  class er constructor er vitoreo parameter hishebe kisu neoya hoi nai.


# shop1 = Shop('gadeget 420')
# print(shop1.shop_name)

# pd = Product('iphone',200000,10)
# print(pd.product_name)
    
shop1 = Shop("apple bd")
shop1.add_product("iphoneX",4000,12)
shop1.add_product("samsung59",40000,50)


# shop1.product_price={} #product_quantity and product_price ke baire theke access kore empty kore fela jasse. tai ai duto ke protected korte hbe (_)=1 underscore_instanceName = protected. (__)=2 underscore__instacnceName = private. protected= parent o child class access korte parbe. baire theke keo access korte parbe na
# shop1.__product_quantity={}

# dictionary guloke private banaye rakhte hbe. jate baire theke keo access ba modify na korte pare

# print(shop1._Store__products_quantity)
# print(shop1._Store__products_price)


shop1.show_products()
shop1.buy_product("iphoneX",2)
shop1.buy_product("iphoneXx",2)

shop1.show_products()
shop1.show_profit()


# shop2 = Shop("only car")
# shop2.add_product("marcedes",100000,7)
# shop2.add_product("ferrari",800,10)
# shop2.show_products()