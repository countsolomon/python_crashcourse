#exercise 9-10

#import the restaurant class
from restaurant import Restaurant

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
