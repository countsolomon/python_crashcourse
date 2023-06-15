from priv import Admin

admin1 = Admin('christopher', 'solomon', 'IT', 27)
admin1.privileges.show_privileges('can read', 'can write', 'can view')