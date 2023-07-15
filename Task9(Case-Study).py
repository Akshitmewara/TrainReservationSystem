# Case Study: Train Reservation System: 
# Description: 
#  Generate a Ticket Reserved for specific Passenger and Train based on inputs read from 
# the user console. 
 
# Module Fields Methods 
# Passenger      
# Train   
# Ticket   
 
#  Tasks: 
# 1. Design the Passenger, Train and Ticket module with fields and methods. 
# 2. Read the Passenger, Train and Ticket Details from the user in console. 
# 3. Print the details of Passenger, Train and Ticket in console. 

class Passenger(object):
    def __init__(self, name, age, Gender):
        self.name = name
        self.age = age
        self.Gender = Gender
        
        
    def passengersdetails(self):
        print("Detail Submitted")
        print(f'''
        Name : {self.name} 
        Age : {self.age} 
        Gender : {self.Gender}''')
        print()
        
        
class Train():
    
    
    train_class = {"vande bharat":["jodhpur","Goa",[1,2,3],"Saturday"]}
    def __init__(self, trainname, destination, origin, Class,day):
        self.trainname = trainname
        self.destination = destination
        self.origin = origin
        self.Class = Class
        self.day = day
        
    def checker(self):
        if self.trainname in self.train_class.keys():
            if self.origin in self.train_class[self.trainname]:
                if self.destination in self.train_class[self.trainname]:
                    if self.Class in self.train_class[self.trainname][2]:
                        if self.day in self.train_class[self.trainname]:
                            return True 
                        else:
                            print("The train is not available in that day. Please try again")           
                    else:
                        print("This train is not having this class. Please try again.")            
                else:
                    print("This train is not going in this destination. Please try again.")
            else:
                    print("This train will not deparcher from this place. Please try again.")
        else:
            print("This train is not available. Please try again.")

    def traindetails(self):
        print()
        print(f'''          
        Train Name : {self.trainname} 
        Destination : {self.destination}
        Origin : {self.origin}
        Class : {self.Class}
        Day : {self.day}''')
        
class Ticket(Train,Passenger):
    ticket_price = {1:2000,2:1000,3:500}
    
    
    def __init__(self,trainname,destination,origin,Class,day,name,age,Gender):
        Train.__init__(self,trainname,destination,origin,Class,day)
        Passenger.__init__(self,name,age,Gender)
        
        
    def display_price(self):
        self.Price = self.ticket_price[self.Class]
        print()
        print('this is your total bill : RS', self.Price)
        print()
        
    def Ticketdetails(self):
        print(self.price, self.Class, self.seatnumber, self.destination, self.origin)
        
    def print_ticket(self):  
        ticket_name = self.name
    
        file = open(f'C://Users//jdhtrainee15//Desktop//Akshit online//Python_online//Case Study//{ticket_name}.txt','w')
        file.write(f'''************Ticket**************
        Name : {self.name}
        Age : {self.age}
        Gender : {self.Gender}
                        
        Train Details:----------
        Name : {self.trainname}
        Destination : {self.destination}
        Origin : {self.origin}
        Class : {self.Class}
        Day of Departure : {self.day}
                        
        Price:---------------
        Your Total Bill is Rs{self.Price}''')
        file.close()
        
    def more_tickets(self):
        destination = self.destination
        file = open(f'C://Users//jdhtrainee15//Desktop//Akshit online//Python_online//Case Study//{destination}.txt','a')
        file.write(f'''************Ticket - {self.name}**************
        Name : {self.name}
        Age : {self.age}
        Gender : {self.Gender}
                        
        Train Details:----------
        Name : {self.trainname}
        Destination : {self.destination}
        Origin : {self.origin}
        Class : {self.Class}
        Day of Departure : {self.day}
                        
        Price:---------------
        Your Total Price is Rs{self.Price}
        
        ''')
        file.close()
        
        
        
print("**************Train Reservation System******************")
number_of_passenger = int(input("How many tickets to books : "))
print()

for i in range(number_of_passenger):
    username = input("Username: ")
    userage = int(input("Userage: "))
    usergender = input("Male / female : ")

    objects = Passenger(username, userage,usergender)
    objects.passengersdetails()

    print("**** Train Details ****")        
    trainname = input("Train name: ")
    origin = input("train origin: ")
    destination = input("train destination: ")
    Class = int(input("Train class name: "))
    day = input("train day: ")

    train = Train(trainname,origin, destination, Class, day)

    if train.checker() == True:
        train.traindetails()
        tick = Ticket(trainname,origin,destination,Class, day, username, userage, usergender)
        tick.display_price()
        user_input = input("Do you want to book the ticket: (Y/N) ")
        if user_input == 'Y' or user_input == 'y':
            if number_of_passenger == 1:
                tick.print_ticket()
                print("Ticket Generated")
            elif number_of_passenger != 1:
                tick.more_tickets()
                print("Ticket Generated With the Filename according to your destination ")
        elif user_input == 'N' or user_input == 'n':
            print("Thanks for visiting our  site")
    else:
        train.checker()
        




