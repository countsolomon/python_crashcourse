#exercise 9-5: login attempts

#copy of exercise 9-3: user class
class User:
    """a simple class to describe a user profile."""
    
    def __init__(self, first_name, last_name, department, age):
        """Initialize the user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.age = age
        self.login_attempts = 0

    
    def describe_user(self):
        """describe the user profile."""
        print(f'the following is the user information: ')
        print(f'\nFirst Name: {self.first_name} ')
        print(f'\nLast Name: {self.last_name}')
        print(f'\nDepartment: {self.department}')
        print(f'\nAge: {self.age}')
        
    def greet_user(self):
        """greet the new user"""
        print(f'\nWelcome to the company ' \
              f' {self.first_name.title()} {self.last_name.title()}') 
        
    def show_login_attempts(self):
        """show the number of login attempts"""
        print(f'The user has logged in {self.login_attempts}')

    def increment_login_attempts(self):
        """add the number of login attempts by 1. 
        simulate the user logging in. 
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset the number of login attempts to 0"""
        self.login_attempts = 0


christopher = User('christopher', 'solomon', 'information technology', 30)
print(christopher.describe_user())
#increment the login attempts by 2
christopher.increment_login_attempts()
christopher.increment_login_attempts()
christopher.show_login_attempts()


#reset the login attempts
christopher.reset_login_attempts()
christopher.show_login_attempts()

