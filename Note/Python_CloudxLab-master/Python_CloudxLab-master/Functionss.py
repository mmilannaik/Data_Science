# Functions in python
# and docstring
# they are use to make our own functions
# to make our work easy

# lets create a simple function
'''
def sum1(a,b):        # this is a very basic example of the function
    print(a + b)
sum1(2,2)
'''

# lets create a proper function
def average_no(a, b):
    ''' This function gives  the average of two numbers'''   # this is the docstring the first line after the def command it tells all about the function
    c = a + b / 2
    return c
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
average = average_no(a, b)
print("the average of user input is ", average)

# how to see a dockstring
print(average_no.__doc__)     # this is a docstring

print(5 % 2)



