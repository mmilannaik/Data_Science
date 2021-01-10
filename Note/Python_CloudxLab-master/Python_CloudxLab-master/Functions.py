# Functions
# Catching Exceptions
# Program 1
# Define a function with name except_func
# which takes one argument with name num and returns its multiplication with itself.
# If the argument passed during the function call is not valid for multiplication,
# return a str with content invalid number.
'''
def except_func(num):
    try:
        num = float(input("Enter a number:\n"))
        mult = num * num
        return mult
    except:
        print("invalid number ")
        num = float(input("Please enter a number:\n"))


except_func(2)

# Program 2
import math


def new_function(num):
    return (num * math.pi)


def void_function(num1, num2):
    print(new_function(math.pow(num1, num2)))


void_function(4.6, 7.3)


# program 3

def add(x, y, z):
    a = x + y + z
    return a


print(add(1, 2, 3))

# program 4
def do_math(a, b, kind='add'):
    if (kind == 'add'):  # if this condition is true then the output will be a + b other wise else condition will run
        return a + b
    else:
        return a - b


do_math(1, 2)

# program 5
# LABELED PARAMETERS IN FUNCTIONS
# For example

def add_num(x, y, z='None'):
    if z == 'None':
        return x + y
    else:
        return x + y + z


print(add_num(1, 2))
print(add_num(1, 2, 3))

# Revising the Function part
# program 6
def hello(Name):
    print("Hello")
    print("How are you ")

print(hello(), "Tom")

try:
    def add(x, y):
        print(x + y)
except:
    print("Please put integer number")

print(add(2, 3))



# program 7
# Lets try a nest function

def calculator(num1, num2):   # functions with arguments
    print("Please write the another function ")


def add(num1, num2):
    print(num1 + num2)


def mult(num1, num2):
    print(num1 * num2)


def sub(num1, num2):
    print(num1 - num2)


def div(num1, num2):
    print(num1 / num2)


def mod(num1, num2):
    print(num1 % num2)


def pow(num1, num2):
    print(num1 ** num2)


print(calculator(2, 2))
print(add(2, 2), div(3, 5), pow(2, 2))   # this way we can use multi functions at a time


# Program 8
# lets try an another simple program
# using both functons and conditions
def country(lang):
    if lang == "eng":
        print("Hello")
        print("England")
    if lang == "hindi":
        print("Namste")
        print("India")
    if lang == "french":
        print("Bonjour")
        print("France")
    if lang == "german":
        print("Guten tag ")
        print("Germany")

    else:
        print("Please type your country ")


print("Please type your language here ")
print(country("german"))


# lets do the program 8 with return type
# program 9

def country(lang):
    if lang == "eng":
        return ("Hello")

    if lang == "hindi":
        return ("Namste")

    if lang == "french":
        return ("Bonjour")

    if lang == "german":
        return ("Guten tag ")


    else:
        return "Please type your country"

print(country("french"))
# with return type we can assign the function value to a variable
# for example
x = country("eng")
print(x)   # this is not possible with print type
'''

# program 10
# rewrite pay computation ( in conditions) with time and a half for over time a create a function called
# computepay which takes two parameters hours and rate
hours = float(input("Enter hours here: "))
rate = float(input("Enter rate here: "))
extra = 0


def compute_pay(hours, rate):
    if hours > 40:
        extra = hours - 40
        hours = 40
        pay = hours * rate + 1.5 * rate * extra
        return pay
    else:
        return hours * rate


print("Pay", compute_pay(hours, rate))

'''
# Program 11
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

def stuff():
    print('Hello')
    return
    print('World')

stuff()
'''


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

print("Thats a simple calculator ")


# Another example of python function
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))
