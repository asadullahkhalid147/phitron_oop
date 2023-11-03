#bus ticket Booking System
#Admin--
# 1) add a new Bus
# 2) Check available bus
# 3) Can check bus info

# user--
# 1) Check available buses
# 2) Can check Bus info
# 3) Can reserve seat

#creating login system--
class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]
        # ['seat'][0]=? orthat seat of 0 er value koto. 
        # ['seat'][1]=? seat of 1 er value koto


b= Bus(2,"Rahim","12PM","12:30PM","Dhaka","Chittagong")
# print(vars(b))#jokhon "b" object ke "vars" function er moddhe diye pass kora hoyese tokhon amader je constructor ba __init__ function ta ase tar left side er orthat self. er gulo hoy gelo "key". ar right side er gulo hoye gelo value


class Phitron:
    total_bus = 5

    total_bus_list = [] # bus er information [{ } { } { } { }] evabe ase,dictionary akare
    def add_bus(self):
        bus_no = int(input("Enter Bus No: "))

        flag=1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print("Bus Already Added")
                flag=0
                break

        if flag:
            bus_driver=input("Enter Bus Driver Name: ")
            bus_arrival = input("Enter Bus Arrival Time: ")
            bus_departure = input("Enter Bus Departure Time: ")
            bus_from = input("Enter Bus Start From: ")
            bus_to = input("Enter Bus Destination: ")

            self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))#vars function use kore new bus ke dictionary hishebe rakhsi
            print("\n Bus added Successfully")

# company = Phitron()
# company.add_bus()

class Counter(Phitron):#counter ;phitron ke inherit korbe
    user_list=[]
    def reservation(self):
        bus_no = int(input("Enter Bus No: "))

        for w in self.total_bus_list:
            if bus_no==w['coach']:
                passenger = input("Ener Your Name: ")
                seat_no = int(input("Enter Seat No: "))

                if seat_no>20:
                    print("No Seats Available")
                elif w['seat'][seat_no-1]!="Empty":
                    print("Seat Already Booked")
                else:
                    w['seat'][seat_no-1]=passenger
            else:
                print("No Bus Available")

        # for bus in self.total_bus_list:
        #     print(bus['seat'])

    def show_ticket(self):
        bus_no = int(input("Enter Bus Number: "))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print('*'*50)#50 ta star por por print hbe
                print()
                print(f"{' '*10}{'#'*10}Bus Info {'#'*10}")
                print(f"Bus Number: {bus_no}\t\t\t Driver :{w['driver']}")
                print(f"Arrival: {w['arrival']}\t\t\t Departure time: {w['departure']}\n From: {w['from_des']}\t\t\t To: \t {w['to']}")

                print()
                
                a=1# a= seat number
                # amader seat 20 ta. tai 5 bar loop cholbe. protibar loop a 4 ta seat dekhano hbe.
                for i in range(5):#    1st n.l     2nd n.l
                    for j in range(2):
                        print(f"{str(a).zfill(2)}.{w['seat'][a-1]}",end="\t")# 1    2     3    4    n.l=nestedLoop
                    # zfill(2) diye 1 ke 01 banano hoyese. 1 digit ke 2 digit banano hoyese
                        a+=1
                    
                    for j in range(2):
                        print(f"{str(a).zfill(2)}.{w['seat'][a-1]}",end="\t")
                        a+=1
                    print()
                print("*"*50)

    def get_users(self):
        return self.user_list

    def create_account(self):
        name = input("Enter Your Username: ")
        password = input("Enput Your Password: ")
        self.new_user = User(name,password)
        self.user_list.append(vars(self.new_user))

    def available_buses(self):
        if len(self.total_bus_list)==0:
            print("No Buses Available\n")
        else:
            print("*"*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10}{'#'*10}Bus {bus['coach']} INFO {'#'*10}")
                print(f"Bus Number: {bus['coach']}\t Driver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']}\t Departure Time: {bus['departure']}\n From: \t {bus['from_des']}\t\t To: \t{bus['to']}")
            

# company = Phitron()
# company.add_bus()
# c = Counter()
# c.reservation()


while True:
    company = Phitron()
    b = Counter()
    print("1.Create An Account\n2.Login to Your Account\n3.Exit")
    user_input = int(input("Enter Your Choice: "))

    if user_input==3:
        break
    elif user_input==1:
        b.create_account()
    elif user_input==2:
        name = input("Enter Your Username: ")
        password = input("Enter Your Password: ")

        flag=0
        isAdmin = False

        if name=="admin" and password=="123":
            isAdmin=True
        if isAdmin==False:
            for user in b.get_users():
                if user['username']==name and user['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print(f"\nWelcome to Bus Ticket Booking System")
                    print("1. Available Buses\n2. Show Bus Info \n 3. Reservation\n4. Exit")
                    a = int(input("Enter Your Choice: "))
                    if a==4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show_ticket()
                    elif a==3:
                        b.reservation()
            else:
                print("No Username Found: Nikal bsdk nikal. pahle fursat me nikal bawre")
        else:
            while True:
                print(f"\n{' '*10}Hello Admin. Welcome to Bus Ticket Booking System")
                print("1. Add Bus\n2. Available Buses \n3. Show Bus Info \n4. Exit")
                a = int(input("Enter Your Choice: "))
                if a==4:
                    break
                elif a==1:
                    b.add_bus()
                elif a==2:
                    b.available_buses()
                elif a==3:
                    b.show_ticket()




                


#Global
    # 1.Create An Account
    # 2.Login To Your Account
    # 3.Exit

    # Admin
    # 1. Add Bus
    # 2. Check if Bus are Available
    # 3. Can check Bus Info

    # User
    # 1.Bus Info
    # 2.Reserve Ticket
    # 3.Available Buses
    # 4.Exist From system