# Try Except and Exception in python
# Exception Handling
# or error handling
# used where there is a high risk of run time error
'''
num1 = input("Enter a number: ")
num2 = input("Enter number: ")
try:
    sum = num1 + num2
    print(sum)
except:
    print("Give a numerical value")

number1 = input("Enter number: ")


try:
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))


except Exception:
    print("Last chance ")
    print("Pleasew enter int values in input")
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    print("correct input")



# lets try an another example
try:
    print(x)
except:
    print("there is no variable such as x")
    print("error occured")


try:  # multi exceptions  more than one exception
    print(x)
except NameError:
    print("an exception has arrived")
except NameError:
    print("unknown exception arrived ")
except:
    print("unknown error")

# we ca use else if there is no error
try:
    print("hello")
except:
    print("error arrived")
else:
    print("no error arrived ")
'''

#
# finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("error occured")
finally:
    print("just run dont care about it ")


a = int(input())
b = int(input())
try:
    print(a/b)
except Exception as e:         # we use exception as e when we have to find about the occured error
    print("can not divide by zero",    e)

print("leave the loop ")