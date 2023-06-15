"""A module that holds a class that represents a Restaurant"""
class Restaurant:
    """a description of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize the restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """a method to describe a restaurant"""
        print(f"This restaurant creates fresh, {self.cuisine_type}.")

    def open_restaurant(self):
        """simulate opening the restaurant"""
        print(f"{self.restaurant_name} is open!")
