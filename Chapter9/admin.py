#The import is required for 9.12 - files imported on a per-file-basis -> if both admin.py and user.py imported into chapter9.py, chapter9.py has access to both, but admin.py doesn't 
#have access to user.py (required by Admin for inheritance). Think of this as creating a chain.
from user import User

class Privileges:                                                                       
    def __init__(self):                                                                 
        self.privileges_list = ['Can add posts', 'Can delete posts', 'Can ban users']   

    def show_privileges(self):
        privileges_text = "\n".join(self.privileges_list)
        print(f"\nAs an Admin, they have the following privileges:\n{privileges_text}")

class Admin(User):
    def __init__(self, forename, surname, age, job):
        super().__init__(forename, surname, age, job)
        self.privileges = Privileges()