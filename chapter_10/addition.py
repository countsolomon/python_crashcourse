#add two numbers

x = input("What is the first number? ")
y = input("What is the second number? ")


try:
    sum = int(x) + int(y)
    print(f"The sum of the two numbers is: {sum}.")
except ValueError:
    print('you probably entered in a string. ')