#exercise 9-1
class Restaurant:
    """a description of a restaurant"""

    def __init__(self, restaurant_name, cuisin_type):
        """initalize the restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisin_type


    def describe_restaurant(self):
        """a method to describe a restaurant"""
        print(f"This restaurant creates fresh, {self.cuisine_type}.")

    def open_restaurant(self):
        """simulate opening the restaurant"""
        print(f"{self.restaurant_name} is open!")


restaurant = Restaurant('restaurant', 'tacos')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# exercise 9-2: Three Restaurants. 
restaurant_2 = Restaurant('solomon\'s fries', 'french fries')
restaurant_3 = Restaurant('kara\'s subs', 'subs')

#call all the methods within the class. 
#custom made restaurants 
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
