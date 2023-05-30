#a program that uses the restaurant class, 
# and makes a subclass about ice cream stand

#exercise 9-1
class Restaurant:
    """a description of a restaurant"""

    def __init__(self, restaurant_name, cuisin_type):
        """initalize the restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisin_type

    def describe_restaurant(self):
        """a method to describe a restaurant"""
        print(f"This restaurant creates fresh, {self.cuisine_type}.")

    def open_restaurant(self):
        """simulate opening the restaurant"""
        print(f"{self.restaurant_name} is open!")
        
class IceCreamStand(Restaurant):
    """a subclass respresenting ice cream stands"""

    def __init__(self, restaurant_name, cuisin_type):
        """initialize the ice cream class"""
        super().__init__(restaurant_name, cuisin_type)
        
    def show_flavors(self, *flavors):
        """accept a list of flavors that are sold at the ice cream stand"""
        print(f'{self.restaurant_name.title()} has the following flavors: ')
        for self.flavor in flavors:
            print(f'- {self.flavor}')

my_first_stand = IceCreamStand('solomons ice cream', 'ice cream')
my_first_stand.show_flavors('chocolate', 'vanilla', 'strawberry', 'blueberry', 'orange')