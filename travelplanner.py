route = []
transportation = []
fun = []
money = []


print("Hello, and welcome to the Bantle Travel Planner!")
name = input("Please start by telling me your name: ")
print(f"\nPleasure to meet you {name}!")

print("Lets begin with figuring out your route and some details. When you have put in all your desired destinations, please type 'Done'.")
destination = input("Enter a stop on your journey: ")

while True:
    if destination.lower() == 'done':
        break

    route.append(destination)
    
    print(f"\n{destination} is a great stop!")
    transport = input("How will you get there? Choose your mode of transport: ")
    transportation.append(transport)

    activity = input(f"\nOkay, and what activities do you want to do in {destination}: ")
    fun.append(activity)

    budget = input(f"\nGreat, sounds like fun! Finally, what is your budget for {destination}: ")
    money.append(budget)

    destination = input("Brilliant! Where to next then: ")

print("\nThis sound like it's going to be a fun trip!")
choice = input("\nBefore I give you the summary of the trip, do you want to make any changes? (Y/N): ")

while True:
    if choice.lower() == 'y':
        choice_place = input("Please enter the stop you wish to edit: ")
        if choice_place in route:
            i = route.index(choice_place)
            route[i] = input(f"Instead of {choice_place}, where do you want to go? ")
            transportation[i] = input("Update your mode of transport: ")
            fun[i] = input(f"What will you do in {route[i]}? ")
            money[i] = input(f"Finally, what is your budget for {route[i]}? ")
            break
        else:
            choice_place = input(f"'{choice_place}' isn't in your plan, please try again: ")

    if choice.lower() == 'n':
        break

    if choice.lower() not in ('y', 'n'):
        choice = input(f"Invalid response, please try again. ")


print("\nWe're finished planning your trip! Here is a summary: ")

for i in range(len(route)):
    print(f"Stop {(i+1)}: {route[i]} \nMode of Transport: {transportation[i]}    Activity: {fun[i]}    Budget: {str(money[i])}\n")

print(f"\nThank you for using the Bantle Travel Planner {name}! Hope you enjoy your trip!")

