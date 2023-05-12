#exercise 9-1
class Restaurant:
    """a description of a restaurant"""

    def __init__(self, restaurant_name, cuisin_type):
        """initalize the restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisin_type


    def describe_restaurant(self):
        """a method to describe a restaurant"""
        print("This restaurant is a taco shack.")

    def open_restaurant(self):
        """simulate opening the restaurant"""
        print("The restaurant is open!")

restaurant = Restaurant('restaurant', 'tacos')
print(f"my restaruants description is {restaurant.describe_restaurant}")
print(restaurant.open_restaurant)