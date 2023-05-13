#chapter 9-3: working with classes. 
#the user class
class User:
    """a simple class to describe a user profile."""
    
    def __init__(self, first_name, last_name, department, age):
        """Initialize the user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.age = age
    
    def describe_user(self):
        """describe the user profile."""
        print(f'the following is the user information:')
        print(f'\nFirst Name: {self.first_name} ')
        print(f'\nLast Name: {self.last_name}')
        print(f'\nDepartment: {self.department}')
        print(f'\nAge: {self.age}')
        
    def greet_user(self):
        """greet the new user"""
        print(f'\nWelcome to the company {self.first_name.title()} {self.last_name.title()}')

#user: jerry white
jerry_white = User('jerry', 'white', 'information technology', '42')
jerry_white.describe_user()
jerry_white.greet_user()

#user: scarlett mcdonald
scarlett_mcdonald = User('scarlett', 'mcdonald', 'accounting', '27')
scarlett_mcdonald.describe_user()
scarlett_mcdonald.greet_user()

    