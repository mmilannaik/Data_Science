# if , else , elif are the conditional statements in the python
# they give the python power to analysis check the condition and give required output
'''
# so lets start
# lets check the greater number among the three numbers
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
if num1 > num2 and num1 > num3:
    print("Num1 is greatest")
elif num2 > num1 and num2 > num3:
    print("num2 is greatest ")
elif num1 == num2 and num1 == num3 and num2 == num3 and num2 == num1:
    print("all numbers are equal")
else:
    print("num3 is greatest ")
'''
# now lets create a condition for driving if age > 18 allowed to drive and if age < 18 not allowed and
# if age == 18 also allowed to drive
'''
age = int(input("Enter age here : "))
if age > 18:
    print("Allowed to drive")
elif age == 18:
    print("Allowed to drive")
else :
    print("Not allowed to drive ")
'''
# lets try another problem
# Take value of length and breadth and decide weather it is rectangle or not
'''
length = float(input("Enter length here : "))
breadth = float(input("Enter breadth here : "))

if breadth == length:
    print("It is a square")
elif breadth > length or breadth < length:    # we dont need this condition still i put it for fun :) :)
    print("this is rectange ")
'''
# another problem
# A shop will give discount of 10% if the cost of purchased price is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user
'''
quantity = int(input("Enter quantity here : "))
cost = 100 # for each quantity
if quantity*100 > 1000:
    print("the cost is", (quantity*100) - (.1*quantity*100))
'''

# the next problem is
#  company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
'''
year_of_service = int(input("Enter years here : "))
salary = float(input("Enter salary here : "))
if year_of_service > 5:
    print("bonus is", .5 * salary)
elif year_of_service == 5:
    print("one more year till bonus")
else:
    print("no bonus")
'''
# next porblem
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
'''
marks = int(input("Enter Marks here : "))
if marks < 25:
    print("the grade is F")
elif marks >= 25 and marks < 45:
    print("the grade is E")
elif marks >= 45 and marks < 50:
    print("the grade is D")
elif marks >= 50 and marks < 60:
    print("the grade is C")
elif marks >=60 and marks < 80:
    print("the grade is B")
else:
    print("the grade is A")
    
'''
# NEXT PROBLEM
# Take input of age of 3 people by user and determine oldest and youngest among them.
'''
a = age1 = int(input("Enter age here : "))
b = age2 = int(input("Enter age here : "))
c = age3 = int(input("Enter age here : "))

if a > b and a > c:
    print("A is oldest ")
elif b > a and b > a:
    print("B is oldest")
elif c > a and c > b:
    print(" c is oldest ")
else:
    print("all are equal ")
'''

#
'''
list1 = [11, 33, 22, 33, 43, 21, 3, 45, 54]
if 11 in list1:
    print("number is present")

for number in list1:
    if number > 15:
        print(number)

if 54 not in list1:  # print statement depends upon the condition
    print("not available ")

'''
# lets try to make a calculator
# a faulty calculator which gives the wrong output for specific numbers and operator
# conditions are available in the code 
#

'''
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Put a operator: ")

if operator == "+":
    if num1 == 56 and num2 == 9:
        print("77")
    else:
        print(num1 + num2)

elif operator == "*":
    if num1 == 45 and num2 == 3:
        print("555")
    else:
        print(num1 * num2)
elif operator == "/":
    if num1 == 56 and num2 == 6:
        print("6")
    else:
        print(num1 / num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "//":  # floor division operator
    print(num1 // num2)
elif operator == "**":  # power operator
    print(num1 ** num2)
'''

# another problem
# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1
'''
num = int(input("Enter number here"))
if num < 0:
    print(num*-1)
else:
    print(num)
'''

# another problem
#
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not
'''
#
classes = int(input("Please enter the number of classes held: "))
attended = int(input("Number of classes attended: "))
percentage = attended * 100 / classes
print(float(percentage), "%")
if percentage >= 75:
    print("Allowed")

else:
    print("Not allowed ")
'''

# lets try another problem
# Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

class_held = int(input("Enter number of classes held: "))
class_atten = int(input("Enter number of classes attended: "))
medical_cause = str.upper(input("Enter medical cause = 'Y' and no medical cause = 'N': "))
percentage = class_atten * 100 / class_held
print(float(percentage), "%")
if percentage >= 75:
    print("Allowed")
elif percentage < 75 and medical_cause == "Y":
    print("Allowed")
else:
    print("Not allowed")
