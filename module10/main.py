from menu import Pizza, Burger,Drinks,Menu
from restaurant import Restaurant
from Users import Chef,Customer,Server,Manager
from order import Order
def main():
    # print('main as cpp')
    menu = Menu()
    pizza_1 = Pizza('shutki pizza',600,'large',['shutki','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('alur vorta pizza',400,'large',['potato','onion','oil'])
    menu.add_menu_item('pizza',pizza_2)

    pizza_3 = Pizza('Dal pizza',500,'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza_3)


    #add burger to the menu
    burger_1 = Burger('Naga Burger',1000,'Chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger',1200,'beef',['goru','haddi'])
    menu.add_menu_item('burger',burger_2)

    #add drinks to the menu
    coke = Drinks('Coke',50,True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Mocha',300,False)
    menu.add_menu_item('drinks',coffee)

    #show Menu
    # menu.show_menu()

    sai_baba_restaurant = Restaurant('sai baba restaurant',2000,menu)

    #add employees
    manager = Manager('kala chan Manager',15601,'kala@cha.com','kaliapur',1500,'jan 1 2020','core')
    sai_baba_restaurant.add_employee('manager',manager)

    chef = Chef('Rustom baburchi',6,'kopa@rustom.com','rustomnagar',3500,'Feb 1 2020','Chef','everything')
    sai_baba_restaurant.add_employee('chef',chef)

    server = Server('Chotu Server',45865,'nai@jai.com','restaurant',200,'march 1, 2020','server')
    sai_baba_restaurant.add_employee('server',server)

    #show employees
    # sai_baba_restaurant.show_employees()


    #customer 1 placing an order
    customer_1 = Customer('Sakib Khan',45896,'king@khan.com','banani',100000)
    order_1 = Order(customer_1,[pizza_3,coke,burger_1,pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    sai_baba_restaurant.add_order(order_1)

    #customer one paying for order_1
    sai_baba_restaurant.receive_payment(order_1,20000,customer_1)
    print('revenue and balance after first customer',sai_baba_restaurant.revenue,sai_baba_restaurant.balance)



    #customer 2 placing an order
    customer_2 = Customer('zayed khan',3000,'zayed@khan.com','gulshan',100000)
    order_2 = Order(customer_2,[pizza_1,burger_2,burger_1,pizza_2,coffee])
    customer_2.pay_for_order(order_2)
    sai_baba_restaurant.add_order(order_2)

    #customer one paying for order_2
    sai_baba_restaurant.receive_payment(order_2,10000,customer_2)
    print('revenue and balance after second customer',sai_baba_restaurant.revenue,sai_baba_restaurant.balance)

    #pay rent
    sai_baba_restaurant.pay_expense(sai_baba_restaurant.rent,'Rent')
    print('after rent',sai_baba_restaurant.revenue,sai_baba_restaurant.balance,sai_baba_restaurant.expense)


    #giving salary to chef
    sai_baba_restaurant.pay_salary(chef)
    print('after salary',sai_baba_restaurant.revenue,sai_baba_restaurant.balance,sai_baba_restaurant.expense)

#call the main
if __name__ =='__main__':
    main()