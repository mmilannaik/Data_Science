# Parameters and arguments
# functions
# parameters and arguments in functions


# problem 1:
# Write a function with name my_function which takes one argument with name number.
# Then, inside the function, write these statements,
# 1 - Store the number in a variable xyz
# 2 - Convert it into str and store it in xyz_str
# 3 - Concatenate cloudxlab to xyz_str
# 4 - print xyz_str
# Test your function by passing an argument 10. It should print 10cloudxlab.

def my_function(number):
    xyz = number
    xyz_str = str(number)
    xyz_str = xyz_str + "cloudxlab"
    print(xyz_str)


# my_function(10)
my_function(10)

# problem 2
# Define a function with name new_function that takes an argument num and returns its multiplication with π.
# Define a void function with the name void_function which takes two arguments num1 and num2
# which makes the call to new_function with an argument as num1 raised to the power of num2.
# Within the void_function print the value returned by the call.
# In a new cell, call void_function with arguments as 4.6 and 7.3.
#
import math


def new_function(num):
    return num * math.pi


def void_function(num1, num2):
    print(new_function(math.pow(num1, num2)))


# new_function(2)

# Problem 3
# Define a function with name input_name that displays a prompt, "What am I studying?"
# Then, within the function take an input from the user and return it.
# In a new cell, call the function, input Python after the prompt.
# Store the returned value in the variable subject.
# Print subject.

def input_name():
    print("What am I studying?")
    i = input()
    subject = input()
    return subject
    subject = (i)


input_name()


# the other way of doing this is

def input_name():
    return (input("What am I studying?"))


subject = input_name()
input_name()


# Problem 4
# using boolean

# Define a function with the name bool_func which take 4 arguments as num1, num2, num3, num4.
# Inside the function, write statements to check,
# 1.) if num1 is greater than num2 and store result in exp1 after converting it into str
# 2.) if num1 is equal to num3 and store result in exp2 after converting it into str
# 3.) if num2 is less than or equal to num3 and store result in exp3 after converting it into str
# 4.) if num4 is not equal to num1 and store the result in exp4 after converting it into str
# 5.) Return the value which is the concatenation of exp1, exp2, exp3, and exp4 respectively.
# If you call the function like this: bool_func(1,2,3,4), it should return 'FalseFalseTrueTrue'


def bool_func(num1, num2, num3, num4):
    exp1 = str(num1 > num2)
    exp2 = str(num1 == num3)
    exp3 = str(num2 <= num3)
    exp4 = str(num4 != num1)
    return (exp1 + exp2 + exp3 + exp4)


bool_func(1, 2, 3, 4)


# Problem 5
# conditional operators

# Define a function with name conditional_statements that takes 4 arguments as num1, num2, num3 and num4.
# Inside the function implement a conditional that checks if all the following conditions are true,
# num1 is less than num2, greater than num3 and equal to num4
# num3 is the smallest of all the other arguments
# num2 is a float value
# num1, num3 and num4 are int values
# If all the above conditions are true return the sum of all numbers else return None.
# You can test your function by calling it using different arguments and printing the result.
# See if it returns the appropriate result.

def conditional_statements(num1, num2, num3, num4):
    if num1 < num2 and num1 > num3 or num1 == num4:
        num3 < num2
        num3 < num1
        num3 < num4
        num2 = float()
        num3 = int()
        num4 = int()
        num1 = int()
        print(num1 + num2 + num3 + num4)
    else:
        print("what have i done")


# print(conditional_statements(1,2.3,0,4))


# another way of doing this is
def conditional_statement(num1, num2, num3, num4):
    if num1 < num2 and num1 > num3 and num1 == num4:
        if num3 < num1 or num2 or num4:
            if (num2(type(float))):
                if (num1 and num3 and num4(type(int()))):
                    print(num1 + num2 + num3 + num4)
    else:
        return None


print(conditional_statement(1, 2.3, 0, 4))


# one more way is
def conditional_statements(num1, num2, num3, num4):
    if num1 < num2 and num1 > num3 and num1 == num4:
        if num3 < num2:
            if type(num2) is float:
                if type(num1) is int and type(num3) is int and type(num4) is int:
                    return num1 + num2 + num3 + num4


print(conditional_statement(1, 2.3, 0, 4))
