# Rewrite your pay computation to give the employee
# 1.5 time the hourly rate for hours worked above 40 hours

hours = int(input("Enter the hours\n"))
rate = int(input("Enter the rate\n"))
extra = 0
if hours > 40:
    extra = hours - 40
    hours = 40
pay = hours * rate + 1.5 * rate * extra
print(pay)


# we will again write this program using try and except

try:
    hours = int(input("Enter hours here\n"))
    rate = int(input("Enter the rate here\n"))
    extra = 0
    if hours > 40:
        extra = hours - 40
        hours = 40
        pay = hours * rate + 1.5 * rate * extra
        print(pay)
except:
    print("Please enter the numerical data")
    hours = int(input("Enter hours here\n"))
    rate = int(input("Enter the rate here\n"))



# try and except with the arguments
x = int(input())
y = int(input())
def add(x,y):
    try:
        print(x+y)
    except:
        print("ooops")