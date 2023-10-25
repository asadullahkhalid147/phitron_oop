class Shop:
    cart=[] #class attribute eta. class attribute shobar moddhe share thakbe.shobgulo instance class attribute ke gonohare use korbe. ai karone hridoy shudu cap ar watch kinleo khalid er product o hridoy te paowa jabe 
    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)          #kono property/attribute  ke access korte hole self.property likhe access korte hoy


# kono attribute ke __init__ ba method er moddhe self. diye declare kora hole bole instance attribute
khalid = Shop('khalid')
khalid.add_to_cart('shoes')
khalid.add_to_cart('phone')
print(khalid.cart)


hridoy = Shop('hridoy')
hridoy.add_to_cart('cap')
hridoy.add_to_cart('watch')
print(hridoy.cart)