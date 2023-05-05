#exercise 8-13
#function that should build a user profile

def build_user(first_name, last_name, **user_info):
    """build a dictionary of a user"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_user('christopher', 'solomon', 
                          occupation = 'Cloud Support Engineer', 
                          age = '29', 
                          interests = 'programming, video games, horror movies, reading')

print(user_profile)