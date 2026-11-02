# 1
count = 0

while count < 5:

    Coffee_Price = 3
    Tea_Price = 2
    Pastry_Price = 4

    coffees = 2
    teas = 1
    pastries = 3

# 2
    Total = ((Coffee_Price * coffees) + (Tea_Price * teas) + (Pastry_Price * pastries))
    print(f"You have ordered {Coffee_Price} coffees, {Tea_Price} teas, and {Pastry_Price} pastries!")

# 3
    if Total >= 20:
        Discount = Total * 0.9
        print(f"As your bill is over £20, you are entitled to a 10% discount! Your new total is {Discount}.")
    else:
        print(f"Your total bill is {Total}.")


        print("Next order please.")

    count = count + 1

#1
while True:
    people = int(input("How many people are buying tickets today? "))

#2 & 3
    count = 1
    total = 0
    price_child = 5.00
    price_adult = 10.00
    price_old = 7.50

    while count < (people + 1):
        age = int(input(f"How old is person {count}? "))
        if age < 12:
            price = price_child
            print(f"As you are under 12 years old, your ticket costs {price_child:.2f}.")
        elif age < 65:
            price = price_adult
            print(f"As you are an adult, your ticket costs {price_adult:.2f}.")
        else:
            price = price_old
            print(f"As you are a senior, your ticket costs {price_old:.2f}.")
#4
        total += price
        count += 1

    if people <= 4:
        print(f"The total price for all tickets is {total:.2f}.")
    elif people > 4:
        total = total * 0.9
        print(f"As you have bought more than 4 tickets, you have been given a 10% discount! The total price for all tickets is {total:.2f}.")



