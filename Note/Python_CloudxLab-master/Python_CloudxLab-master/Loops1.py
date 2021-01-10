#  using more functions
# or checking more conditions using loops
# for example finding a specific number in a list
'''
found = False
for numbers in [12, 34, 464, 343, 23, 565, 78, 23, 23, 565, 454]:
    if numbers == 23:
        found = True
        print(found, numbers)

# another example
# this time the value wiil be a string

found = False
for name in ["messi", "neymar", "vidal", "alonso", "messi1", "pique"]:
    if name == "messi":
        found = True
        print(found, name)
    else:
        print("please type the name of the G.O.A.T")
# there are total 6 names in the list
# so it will give this output
# output :
# True messi  # because it starts checking the list from 0 left to right so first is true and others are false
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T


# lets try an another example of this boolean conditions with user input
name = input("Please enter your name\n")
found = False
if name == "Messi":
    found = True
    print(found, name)
    print("correct right entery")
else:
    found = False
    print(found, "Please try again later ")

'''

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break;
        n = int(num)
        largest = num if largest < num or largest == None else largest
        smallest = num if smallest > num or smallest == None else smallest
    except:
        print("Invalid input")

print("Maximum number is ", largest)
print("Minimum number is ", smallest)