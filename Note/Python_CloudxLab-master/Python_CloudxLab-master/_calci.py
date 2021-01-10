# creating a % calculator
# % calculator for school and college marks


# numbers = int(input("Please enter your numbers: "))


'''
# function for swapping two numbres
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
def swap(a,b):
    tem_num = a
    a = b
    b = tem_num
    print(a,b)

swap(a,b)
'''
'''
# functions to write a table
num1 = int(input("Enter nmuber here: "))
range1 = int(input("Please enter your range here: "))
def table():
    for i in range(1,range1):
        print(num1,"*",i,"=",num1 * i)

table()
'''
'''
# for factorial of a number
n  = int(input("Rnter the numbere here for factorial: "))
def fact():
    factorial = 1
    if n >= 1:
        for i in range(1, n + 1):
            factorial = factorial * i
    print("Factorail of ", n, " is : ", factorial)

fact()




# for fabionaciii series 

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter an integer: "))
for i in range(number):
    print(fibonacci(i))
'''

