#exercise 9-4: number served. 
class Restaurant:
    """a description of a restaurant"""

    def __init__(self, restaurant_name, cuisin_type, number_served):
        """initalize the restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisin_type
        self.number_served = 0 

    def describe_restaurant(self):
        """a method to describe a restaurant"""
        print(f"This restaurant creates fresh, {self.cuisine_type}.")

    def open_restaurant(self):
        """simulate opening the restaurant"""
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self):
        """set the number of customers that have been served."""
        
restaurant = Restaurant('restaurant', 'tacos', '1')
