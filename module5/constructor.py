class Phone:
    manufactured = 'China'#egulo holo attribute


    def __init__(self,owner,brand,price): #this is constructor phone class er
        self.owner=owner
        self.brand = brand
        self.price = price

    def send_sms(self,phone,sms):#eta holo method
        text = f'sending to :{phone}{sms}'
        print(text) 

my_phone = Phone('kala','oppo',5000) #my_phone holo  object. jodio class a parameter nai,kintu constructor a ase.constructor a value set korsi


print(my_phone.owner,my_phone.brand,my_phone.price)#my_phone.owner =instance kintu owner = property


her_phone = Phone('she','iphone',120000)
print(her_phone.owner,her_phone.brand,her_phone.price)

dad_phone = Phone('abbu','nokia',5000)
print(dad_phone.owner,dad_phone.brand,dad_phone.price)