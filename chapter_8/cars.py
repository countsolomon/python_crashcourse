#exercise 8-14 
#car making machine
def make_car(manu, model, **car_info):
    """the machine that makes the car"""
    car_info['manufacturer'] = manu
    car_info['model'] = model 
    return car_info

#call it 
car1 = make_car('mazda','6', 
                feature1 = 'heated seats',
                feature2 = 'bluetooth audio',
                color = 'black' )

car2 = make_car('subaru', 'outback', color = 'blue', tow_package=True)

car3 = make_car('nissan', 'rougue', color = 'black', feature1 = 'heated seats', feature2 = 'digital dash')

print(car1)
print(car2)
print(car3)