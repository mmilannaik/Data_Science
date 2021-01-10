# conditional operators related questions
# write a program to prompt the user for hours and rate per hour to compute gross pay
'''
# lets start
# program 1
hours = float(input("Please enter the hours here\n"))
rate_per_hour = float(input("Please enter the rate here\n"))
gross_pay = hours * rate_per_hour
print("The gross pay is:",gross_pay)


# program 2
# another normal revision or practise program
# lets find a largest number among the three numbers given by the user
number1 = int(input("Please enter number1 here\n"))
number2 = int(input("Please enter number2 here\n"))
number3 = int(input("Please enter number3 here\n"))
if number1 > number2 and number1 > number3:
    print("Number1 is largest")
elif number2 > number1 and number2 > number3:
    print("Number2 is largest")
else:
    print("Number3 is largest ")
print("All are equal or condition not matched ")

# lets try to solve this same question with multiple if condiotion or any other possible way
# progrm 3
num1 = int(input("Please enter number1 here\n"))
num2 = int(input("Please enter number2 here\n"))
num3 = int(input("Please enter number3 here\n"))
if num1 > num2 and num1 > num3:
    print("Number1 is largest")
    if num2 > num3 and num2 > num1:
        print("Number2 is largest")
        if num3 > num1 and num3 > num2:
            print("Number3 is largest")
        else:
            print("All are equal ")
            # not giving suitable answer in unexpected condition
            # what to do ????

# program 4
# another same type of question
number = int(input("Please enter a number "))
if number > 10:
    print("greater")
if number < 10:
    print("smaller")
if number == 10:
    print("equal")

# program 5
# lets make the program 1 more efficient or interactive
# the program 1 is about the rent hour and the gross pay

hours = float(input("Please enter the hours here\n"))
rent = float(input("Please enter the rate here\n"))
gross_pay = hours * rent
if gross_pay > 1000:
    print(gross_pay)
    print("Out of range ")
if gross_pay <= 1000:
    print(gross_pay)
    print("in range ")

print("Got it")

# program 6
# another simple sample program
# we will use arithmatic operators in it

number = int(input("Please enter the number to check the conditions: "))
if number > 5:
    print("number is greater than 5 ")
if number < 11:
    print("number is smaller than 11")
if number == 10:
    print("number is equal to 10")
if number != 8:
    print("number is not wual to 8")


# program 7
# using for condition
for i in range(10):
    print(i)
    if i > 2:
        print("Bigger")
    else:
        print("smaller")
print("program to check which numbers are bigger or which are smaller")

# TRY AND EXCEPT

# program 8
# lets use try and except

try:
    rate = int(input("Please enter the number here "))
except:
    print("Please enter the valid variable type ")
    rate = int(input("Again enter number here"))

# program 9
astr = "Hello"
try:
    istr = int(astr)
except:
    istr -1  # this will show a error


# Program 10
# rewrite your pay computation to give the employee 1.5 times the the hourly rate
# for hours worked above 40
print("Please enter rate and hours here ")
try:
    hours = float(input("Please enter the hours here\n"))
    rate = float(input("Please enter the rate here\n"))
    extra_hour = 0
    if hours > 40:
        extra_hour = hours - 40
        hours = 40
        gross_pay = hours * rate + 1.5 * rate * extra_hour
        print(gross_pay)
    else:
        gross_pay = hours * rate
        print(gross_pay)

except:
    print("Please enter the valid data\nEnter the Float Values")
    hours = float(input("Please enter the hours here\n"))
    rate = float(input("Please enter the rate here\n"))


# program 11
# lets write another program similar to program 10
# the basic blueprint is that if a buyer buys products above a fixed amount they will get
# a specfic discount total price

try:
    print("Please enter the total amount here\n ")
    amount = float(input("Please enter the amount here: "))
    total = 0
    if amount > 10000:
        total = amount - 10000
        discount = 10000 * 30 / 100
        after_amount = amount - discount
        print(after_amount)
    else:
        ramaning_amount = 10000 - amount
        avail_amounnt = str(remaning_amount)  # error here
        print("Please buy products worth" + avail_amounnt + "To avail discount")


except:
    print("Please enter the valid values, check the values again ")
    amount = float(input("Please enter the amount here: "))


# Praogram 12
x = 0
if x < 2:
    print("Small")
elif x < 10:
    print("Medium")
else:
    print("Lage")
print("ALL DONE")

# Program 13
astr = "Hello"
istr = int(astr)
print("First", istr)
astr = "123"
istr = int(astr)
print("Second", istr)

# Program 14
astr = "Hello"
istr = 0
try:
    istr = int(astr)
except:
    istr = -1


# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# finding even and odd number from a list
# list off given number

numbers=[23,56,76,78,90,35,12,45]  #defined a list
for i in numbers:   #for loop use to iterates each number
    if(i%2)==0:
        print (i, "is even")   #print even number
    else:

        print (i, "is odd")     #print odd number

'''



