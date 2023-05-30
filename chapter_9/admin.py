#exercise 9-7 admin class

class User:
    """a simple class to describe a user profile."""
    
    def __init__(self, first_name, last_name, department, age):
        """Initialize the user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.age = age
    
    def describe_user(self):
        print(f'The following information is contained within the users' \
              f'profile')
        print(f'\nFirst Name: {self.first_name} ')
        print(f'\nLast Name: {self.last_name}')
        print(f'\nDepartment: {self.department}')
        print(f'\nAge: {self.age}')
        
    def greet_user(self):
        """greet the new user"""
        print(f'\nWelcome to the company {self.first_name.title()} {self.last_name.title()}')

class Admin(User):
    """a user class speicifically for an Admin user"""
    
    def __init__(self, first_name, last_name, department, age):
        """initialize the admin class"""
        super().__init__(first_name, last_name, department, age)

    def show_privileges(self, *privs):
        """add privileges to the admin users"""
        print(f'The user has the following privileges: ')
        for self.privileges in privs:
            print(f'--{self.privileges}')