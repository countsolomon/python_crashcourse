#a program that uses a function to make sandwiches
#exercise 8-12: sandwiches

def make_sandwich(*args):
    """a function that makes sandwiches"""
    print(f'Creating a sanwich that has the following items: ')
    for item in args:
        print(f" - {item}")

sandwich1 = make_sandwich('pepperoni', 'mushrooms', 'cheese')
sandwhich2 = make_sandwich('cheese', 'onions', 'bologna')
sandwhich3 = make_sandwich('bacon', 'lettuce', 'tomato')
