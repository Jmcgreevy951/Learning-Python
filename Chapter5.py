# 5.1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# 5.2 More Conditional Tests
car = 'ferarri'
print("Is car == to 'Subaru'? I predict False.")
print(car.lower() == 'subaru')

car = input("Please enter a car brand: ")
if car.lower() != 'ferarri':
   print("It's not a ferrari...")
else:
   print("Amazing!")

car = input("Lets go again. Pick another car brand: ")
if car.lower() != 'ferrari' and car.lower() != 'bugatti': #<- ensure to always compare against the variable (ie, car.lower() != 'ferrari'/'bugatti')
   print("Still not a ferrari, or a bugatti...")
else:
   print("Amazing!")

# 5.3 and 5.4 Alien Colors #1 & #2
print("You've shot down an alien ship! You go to the wreckage to find survivors. You find the alien pilot's body.")
alien_colour = input("What colour is it? ")

if alien_colour.lower() in ('yellow', 'green', 'red'): #<- use in instead of or - I put orange in and always came back with 5 points. Unassigned variables are always True
   print("You've earned 5 points! Nice work!")
else:
   print("Not cool bro. 0 points for you!")

if alien_colour.lower() == 'green':
   print("You got a green alien! 5 points!")
elif alien_colour.lower() in ('yellow', 'blue'):
   print("You got a rare alien! 10 points!")
else:
   print(f"The alien you killed was {alien_colour}. They were a member of the galactic alliance. 0 points!")

# 5.6 Stages of Life
age = int(input("Please tell me your age: "))

if age <= 2:
   print("You are a baby")
elif age <= 4:
   print ("You are a toddler")
elif age <= 13:
   print("You are a kid")
elif age <= 20:
   print("You are a teenager")
elif age < 65:
   print("You are an adult")
else:
   print("You are an elder")

# 5.7 Favourite Fruit
favourite_fruits = []

fruit = input("I want to know what your favourite fruits are! Please tell me: ")

while True:    
   if fruit.lower() == 'no':
       break
   else:
       favourite_fruits.append(fruit.lower())
       fruit = input(f"{fruit} is a great fruit! Have you any others? If not, enter 'no'. ")
        
print(favourite_fruits)


favourite_food = False #<- false bullion created to prevent the final message from always showing. if value in list, changes to true

print("Lets see if we like any of the same fruits: ")

if 'strawberry' in favourite_fruits or 'strawberries' in favourite_fruits:
   print("I also love strawberries!")
   favourite_food = True
if 'grape' in favourite_fruits or 'grapes' in favourite_fruits:
   print("I also love grapes!")
   favourite_food = True
if 'orange' in favourite_fruits or 'oranges' in favourite_fruits:
   print("I also love oranges!")
   favourite_food = True
if 'banana' in favourite_fruits or 'bananas' in favourite_fruits:
   print("I also love bananas!")
   favourite_food = True
if not favourite_food: #<- not is the catch all
   print("It doesn't seem like we like any of the same fruits. Conversation terminated...")

# 5.8 Hello Admin, 5.9 No Users
Admin_Names = ['bantle','josh']
Usernames = ['cameron']

if Usernames:
   for user in Usernames:
       print("I can't tell who you are!")
else:
   print("You are the first user to attemp to log in, Welcome!")
user = input("Please enter your username: ")

if user in Admin_Names:
   print(f"Welcome back Admin {user}! ")
elif user in Usernames:
   print(f"Welcome back {user}!")
else:
   print(f"Welcome {user}.")

#5.10 Checking Usernames
current_names = ['josh', 'bantle', 'cameron', 'ross', 'eralp']
new_users = ['mum', 'bean', 'sam', 'josh', 'bantle']

user = input("Welcome! Please enter your username: ").lower()

if user in new_users or user in current_names:
   new_users.remove(user)
   user = input(f"Unfortunately, '{user}' is already a username. Please pick another: ")
   while user in new_users or user in current_names:
       user = input(f"Unfortunately, '{user}' is already a username. Please pick another: ")
   print(f"{user} is a great username!")
   new_users.append(user)
elif user not in new_users or user not in current_names:
   print(f"{user} is a great username!")
   new_users.append(user)

for name in current_names:
   if name.lower() in new_users:
       print(f"Error: '{name}' is a duplicated username. Removing from database...")
       new_users.remove(name)

print(f"Current Users: {', '.join(current_names)}")
print(f"New Users: {', '.join(new_users)}")

# 5.11 Ordinal Numbers
numbers = list(range(1, 101))

for number in numbers:
    if number % 10 == 1:
        print(f"{number}st")
    elif number % 10 == 2:
        print(f"{number}nd")
    elif number % 10 == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
