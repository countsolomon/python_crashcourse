#exercise 8-6 "city names"
def city_country(city, country):
    """a function that returns a city, and country""" 
    formated_city = f"{city}, {country}"
    return formated_city.title()

formated_city_country = city_country(city='Myrtle Beach', country='North America')
print(formated_city_country)