#6.1 Person
person = {
    'first name': 'Cameron',
    'surname': 'McGreevy',
    'age': '26',
    'city': 'Belfast'
    }
print(person)


#6.2 Favourite Numbers
numbers = {
    'Josh': '21',
    'Mum': '15',
    'Cameron': '67',
    'Sam': '69',
    'Henry': '1',
}
print(numbers)


#6.3 Glossary

words = {
   'if': "if:\n This begins an if statement, in which if a value is or isn't equal to something, it runs code to address this.",
   'elif': "elif:\n Used if there are multiple factors to take into consideration - continuation of if statement of sorts.",
   'while': "while:\n Use a while loop to go through each iteration of a list, or while a certain value isn't in the list, do x until it is.",
   'True/False': "True/False:\n Does what it says on the tin - can be used to progress code within a while loop for example.",
   'Ming': "Ming:\n Brotherhood. Ever-lasting loyalty. Family. This is Ming."
}

print(words['if'])
print(words['elif'])
print(words['while'])
print(words['True/False'])
print(words['Ming'])


#6.4 Glossary 2 - BETTER WAY - Shows all values in dictionary using a loop#

#for value in words.values():
#    print(value)
#Where words is the dictionary, . is an 's (ie, Josh's) in English, and values() is the function
#Note: using words.items() gives both the key and the value - Output: ('Ming', 'Ming:\n Brotherhood. Ever-lasting loyalty. Family. This is Ming.') 

#Shows Individual Values That Are Called Upon#
#definition = words.get('if')
#print(definition)

#Printing Only Keys - Note: can leave out .titles(), but without it output won't be capitalised automatically#
#for words in  words.keys():
#   print(words.title())
#Wrap loop in set() to prevent duplicate entries appearing - for words in set(words.keys()):
#This can also be achieved by entering data within {}
#languages = {'python', 'ruby', 'python', 'c'}
#languages
# >>> {'ruby', 'python', 'c'}


#6.5 Rivers
#Note: use .items() instead of .values() here - .values prints both values as one string, where items splits them into 2 seperate items 
rivers = {
   'Thames': 'London',
   'lagon': 'Belfast',
   'Nile': 'Egypt',
   'Nile': 'Egypt'
}

for name, location in set(rivers.items()):
   print(f"The {name.title()} runs through {location.title()}.\n")

#Note: this is a poor solution for this exercise but this is how you deal with key and value
for name, location in set(rivers.items()):
   print(f"{name.title()}")
   print(f"{location.title()}")

for name in rivers.keys():
   print(name.title())

for location in rivers.values():
   print(location.title())


#6.6 Polling
fav_lang = {
   'Josh' : 'English',
   'Cameron' : 'Spanish',
   'Ross' : 'French',
   'Joe' : 'Italian',
   'Mum' : 'Albanian'
}

user = input("Please enter your name:\n")

for name, language in fav_lang.items():
   print(f"Thank you for taking the poll {name.title()}!\nI can see your favourite language is {language.title()}!\n")
   if user not in fav_lang.keys():
       print(f"You haven't taken our poll yet {user}, take our poll now!") 


#6.7 People
people = {  
   'Josh': {
       'Surname' : 'McGreevy',
       'Age' : '21',
       'Animal' : 'Alpaca'
   },
   'Bernadette': {
       'Surname' : 'McGreevy',
       'Age' : '63',
       'Animal' : 'Cow'
   },
   'Ross': {
       'Surname' : 'Gilmore',
       'Age' : '26',
       'Animal' : 'Pig'
   }
}

#Note: [] are used to create a list, but they're also used here to call information from the dictionary within the dictionary (people)
#In previous exercises, nothing was called for from a dictionary within a dictionary, I just went through the dictionary and called for them that way
for user, user_info in people.items():
   full_name = f"{user.title()} {user_info['Surname']}" 
   print(f"This user's full name is {full_name}.")
   print(f"{user.title()} is {user_info['Age']} years old.")

#6.8 Pets - Uses same dictionary and for loop from 6.7
   pet = f"{user_info['Animal']}"
   print(f"{user} has a pet {pet}.\n")

#6.9/6.11 Favourite Places/Cities
places = {
    'Eralp' : {
        'City' : 'Tokyo',
        'Country' : 'Japan',
        'Population' : '~14,000,000',
        'Fact' : 'It is the most populous metropolitan area in the world when the surrounding region is included'
    },
    'Stir-fry' : {
        'City' : 'Plymouth',
        'Country' : 'England',
        'Population' : '~265,000',
        'Fact' : 'The Pilgrims set sail from here aboard the Mayflower in 1620'
    },
    'Ben' : {
        'City' : 'Saintfield',
        'Country' : 'Northern Ireland',
        'Population' : '~3,500',
        'Fact' : 'It was the site of a battle during the 1798 Irish Rebellion'
    },
    'Sam' : {
        'City' : 'Belfast',
        'Country' : 'Northern Ireland',
        'Population' : '~345,000',
        'Fact' : 'The RMS Titanic was built in its shipyards'
    },
}

for name, city in places.items():
    print(f"{name}'s favourite city is {city['City']}, {city['Country']}!")
    print(f"{city['City']} has a population of {city['Population']}.")
    print (f"{city['Fact']}!\n")