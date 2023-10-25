class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self,buyer):
        self.buyer = buyer#self diye ja kisu declare kora hosse ta instance attribute
        self.cart = []

    def add_to_cart(self,item):
        self.cart.append(item)


khalid = Shop('khalid')
khalid.add_to_cart('shoe')
khalid.add_to_cart('phone')

print(khalid.cart)

pranto = Shop('pranto')
pranto.add_to_cart('cap')
pranto.add_to_cart('watch')

print(pranto.cart)
