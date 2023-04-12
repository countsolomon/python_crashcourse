#a function that prints out a default value for cities. 
def describe_city(city, country='North America'):
    """the function that describes a city within the country, that is defined. """
    print(f"\nI would like to go to {city.title()} which in the country of {country.title()}")

describe_city('myrtle beach')
describe_city('oslo', country='Norway')
describe_city('covington')