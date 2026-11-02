#Mini Exercise 
i = 0
places = []

print("Mark Cuban has lent you his United Airlines Golden Ticket, meaning you can fly to 5 places anywhere in the world for free! ")
destination = input("Where do you want to go first? ")
places.append(destination)

while i < 4:
    destination = input(f"{destination} is a great stop! Where to next? ")
    places.append(destination)
    i += 1

#print(places)
#print(sorted(places))
#print(places)
#print(sorted(places, reverse=True))
#print(places)
#places.reverse()
#print(places)
#places.reverse()
#print(places)
#places.sort()
#print(places)
#places.sort(reverse=True)
#print(places)



# 3.1 Lists
count = 0
while count < 5:
   friends = ['Paul', 'Joe', 'Pete', 'Beat', 'Eunan']
   message = f"My friend {friends[count]} is from Belfast!"

   print(message)
   count += 1

while True:
   new_friend = input("Have you any other friends you wish to add to the list? If no, type 'no'. ")
   if new_friend == "no":
       break
   else:
       friends.append(new_friend)

no_friends = 'Eunan'
friends.remove(no_friends)
print(friends)
print(f"My friend {no_friends} isn't from Belfast.")

import time

invite = []
count = 0
count1 = 1
i = 0
dust = 0

invitation = input(f"Bantle is having a party (Bantle's 5 Year Coin Extravaganza) and has graced you with the opportunity of organising! Invite 3 people to Bantle's 5 Year Coin Extravaganza! Who is person {count1}? ") 
invite.append(invitation) 
while count < 2:
    
    count += 1
    count1 += 1
    
    if count > 0:
        invitation = input(f"Fantastic! I'm glad you've invited {invitation} to the party! Who's is person {count1}? ")
        invite.append(invitation)  
print(f"{invite[0]}, {invite[1]}, and {invite[2]} are great people to invite, this party is going to be banging!")

time.sleep(3)

non_friend = invite.pop(2)
new_invitation = input(f"OH NO! I've just received word {non_friend} can't make it to the party! Who will you invite in their place? ")
invite.append(new_invitation)

print(f"The party is saved! I'm pretty sure {new_invitation} and {invite[1]} know each other from primary school, great substitution!")

while i < 3:
    print(f"Sending your invitation to {invite[i]} now...")
    i += 1
    time.sleep(1)

time.sleep(3)

print("THIS JUST IN: Valve have donated a larger table, enough to seat 3 more people total!")

table_invites = input("Who are you inviting first? ")
invite.insert(0, table_invites)

table_invites1 = input("Who are you inviting next? ")
invite.insert(3, table_invites1)

table_invites2 = input("Who gets the final seat at the table? ")
invite.append(table_invites2)

print(f"You have invited {len(invite)} people. This is going to be a great party, worthy of Bantle's 5 Year Coin!")
print(f"Sending invites to {invite[0]}, {invite[3]} and {invite[-1]} now...")
time.sleep(2)
print("Invitations sent :)")

time.sleep(3)

print("Oh no!")
time.sleep(1)
print("I've spoken with the organiser, and they forgot to get extra seats! We only have 3 seats total, so we have to uninvite 4 people - awkward!")

time.sleep(2)

uninvite = input("Who are we uninviting first? ")

while uninvite not in invite:
    print(f"You haven't invited {uninvite}. Pick someone you invited previously.")
    uninvite = input("Try again: ")

invite.remove(uninvite)

while dust < 3:
    print(f"Great choice! {uninvite} is terrible craic! I'm uninviting {uninvite} now... ")
    uninvite = input("Who's next? ")
    
    while uninvite not in invite:
        print(f"You haven't invited {uninvite}. Pick someone you invited previously.")
        uninvite = input("Try again: ")
    
    invite.remove(uninvite)
    dust += 1
    
print(f"That was tough, but I'm glad you chose {invite[0]} and {invite[1]} to come to the dinner!")
time.sleep(2)
print("As Bantle's 5 Year Coin Extravaganaza is such a high profile event, word of the others getting uninvited will surely make headlines tomorrow!")
time.sleep(3)
print(f"I'm going to send messages to {invite[0]} and {invite[1]} to let them know the party is still on.")
print(f"Sending confirmation message to {invite[0]}...")
time.sleep(1)
print(f"Sending confirmation message to {invite[1]}...")
time.sleep(3)
print("Just got a message from Bantle! He says thank you for organising his party!")