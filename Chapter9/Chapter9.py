class Resturants:                     #Resturants is the class -> This is the instructions for creating each individual/instance (in this case, each resturant)
   def __init__(self, name, food):   #__init__ initiates the mechanisms to create an instance 
       self.name = name              #self is used to identify this particular instance, and call upon data for said instance
       self.food = food

   def describe_resturant(self):
       print(f"My resturant is called {self.name}.\nHere we serve {self.food}, please have a look at our menu!")

   def open_resturant(self):
       print(f"{self.name} is open! Come in!")
        
my_resturant = Resturants('BooJosh', 'Mexican')

my_resturant.describe_resturant()
my_resturant.open_resturant()

9.2 Three Resturants
class Resturants:
   def __init__(self, name, food):
       self.name = name
       self.food = food

   def describe_resturant(self):
       print(f"\nThe resturant is called {self.name}.\nHere we serve {self.food}, please have a look at our menu!")

   def open_resturant(self):
       print(f"\n{self.name} is open! Come in!")
        
my_resturant = Resturants('BooJosh', 'Mexican')
their_resturant = Resturants('Cam Dory', 'Fish & Chips')
subweezy_resturant = Resturants('Subweezy', 'Sandwiches')

my_resturant.describe_resturant()
my_resturant.open_resturant()

their_resturant.describe_resturant()
their_resturant.open_resturant()

subweezy_resturant.describe_resturant()
subweezy_resturant.open_resturant()

9.3 Users
class User:
    def __init__(self, forename, surname, age, job):
        self.fullname = f"{forename} {surname}"
        self.age = age
        self.job = job
    
    def describe_user(self):
        print(f"\nUser information:\n")
        print(f"Name - {self.fullname}")
        print(f"Age - {self.age}")
        print(f"Job - {self.job}")

    def greet_user(self):
        print(f"Hello {self.fullname}!")

user_josh = User('Josh', 'McGreevy', 24, 'Manufacturing Technologist')
user_cameron = User('Cameron', 'McGreevy', 27, 'Computer Programmer')
user_finley = User('Finley', 'McGrath', 24, 'Graphic Designer')

user_josh.describe_user()
user_josh.greet_user()

user_cameron.describe_user()
user_cameron.greet_user()

user_finley.describe_user()
user_finley.greet_user()

9.4 Number Served
class Resturants:                 
    def __init__(self, name, food):   
       self.name = name              
       self.food = food
       

    def describe_resturant(self):
       print(f"My resturant is called {self.name}.\nHere we serve {self.food}, please have a look at our menu!")
       
    def open_resturant(self):
       print(f"{self.name} is open! Come in!")
    
    def set_number_served(self):
        self.number_served = 20
        print(f"\nWe have served {self.number_served} people!")
        #customer = int(input("How many people are with you today? ")) #Reminder: input always produces a string, convert to integer with int()
        #self.number_served += customer                                #add customer ONTO the running total, store it back in self.number_served
        #return self.number_served                                     #return the updated total (self.number_served), not customer — customer was just the amount added in; the total is the useful result
    
    def increment_number_served(self):
        customer = int(input("How many people are with you today? "))
        self.number_served += customer
        print(f"\nWe have now served {self.number_served} people!")


my_resturant = Resturants('BooJosh', 'Mexican')

my_resturant.describe_resturant()
my_resturant.open_resturant()
my_resturant.set_number_served()
my_resturant.increment_number_served()

9.5 Login Attempts
class User:
    def __init__(self, forename, surname, age, job):  # Reminder: A parameter is a value handed in when you create the object. It’s temporary, only existing inside __init__, while the method runs, then it’s gone 
        self.fullname = f"{forename} {surname}"       # <- Reminder: These are attributes
        self.age = age                                # <-
        self.job = job                                # <-
        self.login_attempts = 0                       # <-
    
    def describe_user(self):
        print(f"\nUser information:\n")
        print(f"Name - {self.fullname}")
        print(f"Age - {self.age}")
        print(f"Job - {self.job}")

    def greet_user(self):
        print(f"Hello {self.fullname}!")

    def increment_login_attempts(self): #Reminder, always identify self
        self.login_attempts += 1
        print(f"Login Attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login Attempts: {self.login_attempts}")


user_josh = User('Josh', 'McGreevy', 24, 'Manufacturing Technologist')
user_cameron = User('Cameron', 'McGreevy', 27, 'Computer Programmer')
user_finley = User('Finley', 'McGrath', 24, 'Graphic Designer')

user_josh.describe_user()
user_josh.increment_login_attempts()
user_josh.increment_login_attempts

user_cameron.describe_user()
user_cameron.increment_login_attempts()
user_cameron.increment_login_attempts()
user_cameron.increment_login_attempts()
user_cameron.increment_login_attempts()
user_cameron.reset_login_attempts()
user_cameron.greet_user()

user_finley.describe_user()
user_finley.increment_login_attempts()
user_finley.increment_login_attempts()
user_finley.reset_login_attempts()
user_finley.greet_user()()
user_josh.increment_login_attempts()
user_josh.greet_user()
user_josh.reset_login_attempts()

user_cameron.describe_user()
user_cameron.increment_login_attempts()
user_cameron.increment_login_attempts()
user_cameron.increment_login_attempts()
user_cameron.increment_login_attempts()
user_cameron.reset_login_attempts()
user_cameron.greet_user()

user_finley.describe_user()
user_finley.increment_login_attempts()
user_finley.increment_login_attempts()
user_finley.reset_login_attempts()
user_finley.greet_user()

9.6 Ice Cream Stand
class Resturants:                     
   def __init__(self, name, food):   
       self.name = name              
       self.food = food

   def describe_resturant(self):
       print(f"My resturant is called {self.name}.\nHere we serve {self.food}, please have a look at our menu!")

   def open_resturant(self):
       print(f"{self.name} is open! Come in!")

class IceCreamStand(Resturants):                        #Ensure to call the parent class when making the child (Resturants)
    def __init__(self, name, food):
        super().__init__(name, food)
        self.flavours = ['Strawberry', 'Vanilla', 'Chocolate']
        
    def describe_flavours(self):
        flavours_text = ", ".join(self.flavours)        #.join() joins list into one string - joined by ", "
        print(f"Our flavours include: {flavours_text}")
        
my_resturant = Resturants('BooJosh', 'Mexican')
my_ice_cream = IceCreamStand('Josh Scoops', 'Ice Cream')

my_resturant.describe_resturant()
my_resturant.open_resturant()

my_ice_cream.describe_resturant()
my_ice_cream.describe_flavours()

9.7 Admin
class User:
    def __init__(self, forename, surname, age, job):
        self.fullname = f"{forename} {surname}"
        self.age = age
        self.job = job
    
    def describe_user(self):
        print(f"\nUser information:\n")
        print(f"Name - {self.fullname}")
        print(f"Age - {self.age}")
        print(f"Job - {self.job}")

    def greet_user(self):
        print(f"Hello {self.fullname}!")

class Admin(User):
    def __init__(self, forename, surname, age, job):
        super().__init__(forename, surname, age, job)
        self.privileges = ['Can add posts', 'Can delete posts', 'Can ban users']

    def show_privileges(self):
        privileges_text = "\n".join(self.privileges)
        print(f"\nAs an Admin, {self.fullname} has the following privileges:\n{privileges_text}")

user_josh = User('Josh', 'McGreevy', 24, 'Manufacturing Technologist')
user_cameron = User('Cameron', 'McGreevy', 27, 'Computer Programmer')
user_finley = User('Finley', 'McGrath', 24, 'Graphic Designer')
user_admin = Admin('Ross', 'Gilmore', 200, 'Admin')

user_josh.describe_user()
user_josh.greet_user()

user_cameron.describe_user()
user_cameron.greet_user()

user_finley.describe_user()
user_finley.greet_user()

user_admin.describe_user()
user_admin.show_privileges()

9.8 Privileges
class User:
    def __init__(self, forename, surname, age, job):
        self.fullname = f"{forename} {surname}"
        self.age = age
        self.job = job
    
    def describe_user(self):
        print(f"\nUser information:\n")
        print(f"Name - {self.fullname}")
        print(f"Age - {self.age}")
        print(f"Job - {self.job}") 

    def greet_user(self):
        print(f"Hello {self.fullname}!")

class Privileges:                                                                       #Doesn't inherit from anything - Privileges isn't a user, more 'admin has', not 'than is'
    def __init__(self):                                                                 #Only (self) needed, as no privilege parameter is carried over from another class - it's created in the next function...
        self.privileges_list = ['Can add posts', 'Can delete posts', 'Can ban users']   #Only take parameter if you'll use the value

    def show_privileges(self):
        privileges_text = "\n".join(self.privileges_list)
        print(f"\nAs an Admin, they have the following privileges:\n{privileges_text}")

class Admin(User):
    def __init__(self, forename, surname, age, job):
        super().__init__(forename, surname, age, job)
        self.privileges = Privileges()                                                  #Privileges created with empty brackets (no arguement) as Privileges takes nothing. Stores Privileges as an attribute ('admin has/has a') 


user_josh = User('Josh', 'McGreevy', 24, 'Manufacturing Technologist')
user_admin = Admin('Ross', 'Gilmore', 200, 'Admin')

user_josh.describe_user()
user_josh.greet_user()

user_admin.describe_user()
user_admin.privileges.show_privileges() #Dots like a file directory -> /

9.9.1, 2 & 3 Rebuilding Chapter 9 Car Examples From Scratch
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_models(self):
        self.descriptive_name = f"{self.year} {self.make} {self.model}" #Remember: you can't carry variable (ie, descriptive_name) between methods. use self. to enable this
        print(f"My car is a {self.descriptive_name}!")                  #Note: This should really be added under def __init__. If this method isn't run, read_odometers would crash as self.descriptive_name is never created 

    def read_odometer(self):
        print(f"My {self.descriptive_name} has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f"My car now has {self.odometer_reading} miles on it.")
        else:
            print(f"You can't roll back your odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print(f"After my last drive, my {self.descriptive_name} now has {self.odometer_reading} miles on it.")

class Battery:
    #9.9.2 Answer def __init__(self, battery_size=75): #Remember: if the user doesn't give a value, battery_size will default to 75 
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The battery size of my car is {self.battery_size}-kWh.")

    def get_range(self):
        battery_range = round(95 + (self.battery_size * 2.2))
        print(f"The range of your battery is {battery_range} miles")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"We have upgraded your battery size to 100-kWh")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery=75): 
        super().__init__(make, model, year)
        self.battery = Battery(battery) #See notes in 9.8 Priveleges

9.9.1
josh_car = Car('Vaulkswagen', 'Urban Fox', 2007)

josh_car.get_descriptive_models()
josh_car.read_odometer()
josh_car.update_odometer(100)
josh_car.increment_odometer(10)

9.9.2
josh_electric = Battery()

josh_electric.describe_battery()
josh_electric.get_range()

9.9.3
josh_tesla = ElectricCar('Tesla', 'Model S', 2017)

josh_tesla.get_descriptive_models()
josh_tesla.battery.describe_battery()
josh_tesla.battery.get_range()

9.9 Battery Upgrade
josh_tesla = ElectricCar('Tesla', 'Model S', 2017)

josh_tesla.battery.describe_battery()
josh_tesla.battery.get_range()
josh_tesla.battery.upgrade_battery()
josh_tesla.battery.describe_battery()
josh_tesla.battery.get_range()

9.10 Imported Resturant
from resturants import Resturants

josh_resturant = Resturants("McGreevy's", 'Fast Food')

josh_resturant.describe_resturant()
josh_resturant.open_resturant()

9.11 Imported Admin
from admin import Admin
user_admin = Admin('Ross', 'Gilmore', 200, 'Admin')

user_admin.privileges.show_privileges()

9.12 Multiple Modules
from admin import Admin

user_admin = Admin('Ross', 'Gilmore', 200, 'Admin')

user_admin.privileges.show_privileges()

9.13 Dice
from random import randint    #randint -> Random number generator within python
# a = 0
# b = 0
# c = 0

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides) #This line determines the range of the random number generator
        print(f"{roll}")

my_die = Die()
my_ten_die = Die(10)
my_twenty_die = Die(20)

# while a < 10:               #<- This method works, but the below loop is cleaner
#     my_die.roll_die()
#     a += 1
# print()

# while b < 10:
#     my_die.roll_die()
#     b += 1
# print()

# while c < 10:
#     my_die.roll_die()
#     c += 1

for i in range(10):           #No need to assign i to 0 as range() in for loop keeps assigning values (0-9)
    my_die.roll_die()
print()

for i in range(10):
    my_ten_die.roll_die()
print()

for i in range(10):
    my_twenty_die.roll_die()

9.14 Lottery
from random import choice #Choice() takes in a list or tuple and returns a random value

pool = (6, 12, 15, 34, 47, 51, 67, 79, 80, 93, 'A', 'E', 'K', 'O', 'V')
winning_list = []

for i in range(4):
    winners = choice(pool)
    winning_list.append(winners)


print("Any ticket matching these wins a prize:", *winning_list, sep=" ") #<- Two things happening here: * removes the [] of print(f"{winning_list})/unpacks list, sep="" works like join - determines
                                                                         #    what's between items in list (can also be ", " for example) 

9.15 Lottery Analysis
from random import choice 
x = 0

pool = (6, 12, 15, 34, 47, 51, 67, 79, 80, 93, 'A', 'E', 'K', 'O', 'V')
winning_list = []
my_ticket = []

for i in range(4):
    winners = choice(pool)
    winning_list.append(winners)

print("Any ticket matching these wins a prize:", *winning_list, sep=" ")

while my_ticket != winning_list:
    my_ticket = []                     #Reminder: ensure ticket is always reset - without, 4 new items will be added indefinitely (winning_list only has 4 items total)
    for i in range(4):
        my_ticket.append(choice(pool))
    x += 1

print(f"Generating your winning ticket\n")
print(f"It took {x} attempts to generate your winning ")
