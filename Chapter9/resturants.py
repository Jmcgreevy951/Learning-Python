class Resturants:
   def __init__(self, name, food):
       self.name = name
       self.food = food

   def describe_resturant(self):
       print(f"\nThe resturant is called {self.name}.\nHere we serve {self.food}, please have a look at our menu!")

   def open_resturant(self):
       print(f"\n{self.name} is open! Come in!")