#8.1 Message
def display_message():
   print("In this chatper, I'm learning about functions and variables!")

display_message()

#8.2 Favourite Book
def favourite_book(title):
   """Display Title of Favourite Book"""
   print(f"Your favourite book is {title.title()}")
favourite_book('Clockwork Orange')

#Practice stuff - shows you can assign (multiple) variables to use in your function#
book = input("Please enter the title of your favourite book: ")
year = input("What year was this book written? ")
def favourite_book(book, year):
   print(f"Your favourite book is {book.title()}! It was written in {year}!")

favourite_book(book, year)

#8.3 T-Shirt
print("Welcome! Let's make you a shirt.\n")

size = input("What size will your shirt be? ")
colour = input("What colour will your shirt be? ")
word = input("What will your shirt say? ")

def make_shirt(size, colour, word):
   print(f"\nYou have decided to make a size {size} {colour} shirt")
   print(f"that says {word}.\n")
   print("Very cool!")

make_shirt(size, colour, word)

#8.4 Large T-Shirts
print("Welcome! Let's make you a shirt.\n")

#Note: .lower() removes capitalisation, .upper() does the opposite
size = input("What size will your shirt be: small, medium or large? ").lower()
colour = input("What colour will your shirt be? ")

def make_shirt(size, colour):

   if size == 'large':
       word = 'I love python!'
   else:
       word = input("What will your shirt say? ")

   print(f"\nYou have decided to make a size {size} {colour} shirt")
   print(f"that says {word}.\n")
   print("Very cool!")

make_shirt(size, colour)

#8.5 Cities
i = 0
def describe_city(name, country):
   print(f"\n{name.title()} is in {country.title()}!")

print("I want to know your favourite city and country!")
print("For example, if you said your favourite city was Reykjavik, which is in Iceland, I will print:")
describe_city('Reykjavik', 'Iceland')

while i != 3:
   name = input("\nWhat is your favourite city? ")
   country = input(f"Which country is {name.title()} in? ")

   describe_city(name, country)

   i = i+1

print("\n\nThank you for participating!")

#8.6 City Names
def city_country(city, country):
   place = f"{city}, {country}"
   return place.title()

#    Note: A variable used only once (places) can be skipped by returning its value directly; naming it is optional and only worth doing when it makes the code clearer
#    Walk the value's journey on one loop when return is used, say paris/france:
#    1. Inside the function, place is built: "Paris, France". But it's trapped in there — the moment the function ends, that variable is destroyed.
#    2. return place.title() throws the value "Paris, France" over the wall, out of the function, just as the function shuts down.
#    3. Outside, result = city_country(...) catches that thrown value and stores it in a fresh variable that lives out here.

i = 0
while i < 3:
   city = input("Please enter the name of your city: ")
   country = input("Please enter the name of the country this city is in: ")
   result = city_country(city, country)
   print(f"{result}\n")
   i = i + 1

#8.7 Album
def make_album(artist, album, release=None):
   music = {'name': artist, 'record': album}
   if release.lower() != 'n/a':
       music['release'] = release
   return music

i=0
while i < 3:

   artist = input("Please enter your favourite musician: ")
   album = input(f"Please enter your favourite album by {artist.title()}: ")
   print(f"What year was {album.title()} released?")
   release = input(f"If you don't know, write N/A: ")
   result = make_album(artist, album, release=release)
   print(f"\n{result}\n")
   i = i+1

#8.9 Messages
texts = [
   'Hello there!',
   'Well horse',
   'My name is Josh'
   ]

def show_messages(texts):
   for text in texts:
       print(f"{text}\n")

show_messages(texts)

#8.10 Sending Messages
texts = [
   'Hello there!',
   'Well horse',
   'My name is Josh'
   ]
sent_texts = []

def send_messages(texts, sent_texts):
   while texts:
       sending = texts.pop()
       print(f"{sending}\n")
       sent_texts.append(sending)

send_messages(texts, sent_texts)

print(texts)
print(sent_texts)

# 8.11 Archived Messages
texts = [
   'Hello there!',
   'Well horse',
   'My name is Josh'
   ]
sent_texts = []

def send_messages(texts, sent_texts):
   while texts:
       sending = texts.pop()
       print(f"{sending}\n")
       sent_texts.append(sending)

send_messages(texts[:], sent_texts)

print(texts)
print(sent_texts)

#8.12 Sandwiches
def sandwich_order(*fillings): #Note: Args (*) store variables (only defined through function call) in tuples
   print("\nHere are the fillings in your sandwich:")
   for filling in fillings:
       print(f"- {filling}")

sandwich_order('chicken')
sandwich_order('chicken', 'lettuce')
sandwich_order('bacon', 'lettuce', 'tomato')

#8.13 User Profile
def build_profile(f_name, l_name, **details): #Note: Kwargs (**) store a pair of key values (eg, age=24) in a dictionary, also defined through function call
   full_name = f'{f_name} {l_name}'
    
   print(f"\nHere are details about {full_name}:")
   print(f"Name: {f_name}")
   print(f"Surname: {l_name}")
   
   for detail in details:
       print(f"{detail.title()}: {details[detail]}") #Note: remember, dictionary logic (key + value) apply to kwargs

build_profile('Josh', 'McGreevy', age=24, location='Northern Ireland')

#8.14 Cars
def car_profile(make, model, **information):
   car = {'make': make, 'model': model}
#FAST VERSION - TAUGHT IN CHAPTER 9 -> car.update(information) #Note: .update() adds information from one dictionary (information kwarg) and moves it into another (car)
#    for key, value in information.items(): #remember, .items takes both key and value
#        car[key] = value # sets it up as a dictionary entry (key + value)
#    return car

result = car_profile('VW', 'Urban Fox', year=2007, mileage=110000)

print(result)

#8.15 Printing Models
import user_profile as up

up.build_profile('Josh', 'McGreevy', age=24, location='Northern Ireland')

#8.16 Imports
#1. from music import make_album as make
from music import *

i=0
while i < 3:

    artist = input("Please enter your favourite musician: ")
    album = input(f"Please enter your favourite album by {artist.title()}: ")
    print(f"What year was {album.title()} released?")
    release = input(f"If you don't know, write N/A: ")
#1.    result = make(artist, album, release=release)
#2.    result = make_album(artist, album, release=release)
    print(f"\n{result}\n")
    i = i+1
