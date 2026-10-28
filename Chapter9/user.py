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
