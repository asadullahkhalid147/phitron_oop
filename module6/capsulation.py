# encapsulation: hide details
# access modifier: public,protected,private
class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name = holder_name#public attribute
        # self.balance = initial_deposit
        # normal vabe kono attribute declare korle sheta public.jemon holder name ekta public attribute. kintu ekhane __balance ekta private attribute. karon eke baire theke access kora jae na
        self.__balance = initial_deposit#private
        self._branch = 'banani11'#protected

    def deposit(self,amount):
        self.__balance +=amount

    def get_balance(self):
        return self.__balance
    
    # def get_balance(self):
    #     return self.__balance
    
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance = self.__balance-amount
            return amount
        else:
            return f'Fokira taka nai'


rafsan = Bank('Chotu',10000)

# print(rafsan.holder_name)
rafsan.deposit(40000)
print(rafsan.get_balance())
rafsan._branch='khilgaon'#(_) ekta underscore diye like bujano hoy sheta protected variable. 
print(rafsan._branch)

print(rafsan.withdraw(5000))

print(dir(rafsan))
print(rafsan._Bank__balance)

