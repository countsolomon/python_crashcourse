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

    def read_customers(self):
        """print the number of customers served. """
        print(f'The number of customers that have been served is {self.number_served}')
    
    def set_number_served(self, num_of_cust):
        """
        set the number of customers that have been served.
        reject if the number is lower then the customers that have been served.
        """
        if num_of_cust >= self.number_served:
         self.number_served = num_of_cust
        else:
            print('you cant remove customers!')

    def increment_number_served(self, add_to_cust):
        """a method that will allow you to add additonal amount of customers"""
        self.number_served += add_to_cust
        
restaurant = Restaurant('restaurant', 'tacos', '1')
restaurant.set_number_served(4)
restaurant.read_customers()

#adding more customers
restaurant.increment_number_served(3)
restaurant.read_customers()