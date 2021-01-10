# Problem 2
'''
Define a function with the name special_func which takes an argument num
Initialize a variable total with value 0
Check if num is positive int.
If num is positive int, find out all the factors of that number and return the sum of odd factors i.e.
total of all factors which are odd. (Factors are the numbers you multiply together to get the number equal to num).
For example, the factors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. Out of which only 1 and 3 are odd ,
So the total(sum of odd factors) here should be '4'
if num is negative or if the type of num is not int then return -10.

Sample Input:
special_func(12)
special_func(15)
special_func(-1)
special_func('abcd')

Sample Output:
4
24
-10
-10
'''

'''

def special_func(num):
    if type(num) is int and num > 0:
        sum = 1  # 1 is always a factor
        i = 3  # because 2 will be a even facotor
        while i <= num:
            if num % i == 0 and i % 2 != 0:
                sum = sum + i
            i = i + 1
        return sum
    else:
        return -10


print(special_func(24))
'''

# problem 3
# Define a function with the name sum_func that takes one argument.
# Return -1 if the argument is not int
# If the argument is an int and if it is non-negative, return the sum of all integers from 0 to that argument.
# In case, the argument passed is negative int, return -1.
# Sample Input:
# sum_func(10)
# sum_func(-1)
# sum_func('abcd')
# Sample Output:
# 55
# -1
# -1
''''
def sum_func(a):
    if type(a) is int:
        if a < 0:
            return -1
        else:
            sum = 0
            integer = 0
            while integer <= a:
                sum = sum + integer
                integer = integer + 1
            return sum
    else:
        return -1


a = 10
print(sum_func())
'''

# Problem 4
# Define a function with the name str_func that takes one argument and returns the
# last character of the string passed to the function as a parameter.
# Sample Input:
# str_func('1234')
# Sample Output:
# '4'

# Define another function with the name sum_str_func that takes one argument
# and returns the sum of all digits in that number.
# The argument passed can be str or an int.
# You need to convert the integer to a string to calculate it's length,
# and then use a loop to add each digit to calculate the sum of all digits.
# Sample Input:
# sum_str_func('1234')
# Sample Output:
# '10'
'''
def str_func(string):
    length = len(string)
    return string[length - 1]


def sum_str_func(num):
    num = str(num)
    total = 0
    index = 0
    length = len(num)
    while index < length:
        digit = int(num[index])
        total = total + digit
        index = index + 1
    return total

print(str_func('1234'))
print(sum_str_func("12345"))

'''

# Problem 5
# Define a function with the name slicing_func that takes an argument (assume string)
# It should print the result after slicing the string without mentioning both the 1st and 2nd elements.
# Sample Input:
# slicing_func("Hello World")
#
# Sample Output:
# llo World
'''
def slicing_func(a):
    value = str(a)
    print(a[2:])


print(slicing_func("Hello World"))

# Problem 6
# Understand and write this code in the notebook and observe you receive,

a = "cloudxlab"
a[1] = 'm'
print(a)

'''


# Problem 7
# If we do not mention anything, find returns the position of the substring that occurs for the first time.
# Define a function with the name email_func that takes a str argument and extracts out and returns the first email id.
# If there is no email id present return None.
# Return only if there is valid email id. An email id is valid if at least one @ is present in it and no blank spaces.
# Else, you can return None.
# Sample Input -
# email_func("Crazy Frog")
# email_func("this is first abhinav@cloudxlab.com and this is second sandeep@cloudxlab.com")
# Sample Output -
# It should return None
# abhinav@cloudxlab.com
'''

def email_func(content):
    position = content.find('@')
    index = position
    if position != -1:
        while index >= 0 and content[index] != ' ':
            index -= 1
        first_part = content[index + 1:position]
        ending_position = content.find(' ', position)
        if ending_position == -1:
            second_part = content[position:]
        else:
            second_part = content[position:ending_position]
        return first_part + second_part
    else:
        return None


print(email_func("google@google.com"))
'''
# Problem 8

# Define a function with the name str_list_func that takes an argument (assume str).
# Interchanges the 1st and last letter of each word in that argument and then return the resulting string.
# i.e. l and g in leaning should be interchanged with each other
# and rest of the letters in that word should remain at their position only (learning will become gearninl)

# Sample Input: 'I am learning Python at CloudxLab'
# Sample Output: 'I ma gearninl nythoP ta bloudxLaC'

def str_list_func(assume_str):
    position = assume_str[1] = assume_str [-1]
    print(assume_str)
    return
assume_str = "raghu"
print(str_list_func(assume_str))

print(assume_str())
