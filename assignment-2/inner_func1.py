class Bank:
    def __init__(self,money) -> None:
        self.money=money

    def depo(self,total_amount):
        def is_amount():
            return total_amount>0
        
        if is_amount():
            self.money+=total_amount