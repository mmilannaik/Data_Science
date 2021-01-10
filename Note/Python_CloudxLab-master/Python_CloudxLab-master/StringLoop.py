# counting the list
# by using the loop
'''
count = 0
print("count")
for numbers in [2, 5, 6, 4, 3, 2, 4, 6]:
    print("numbers")
    count = count + 1
    print(count, numbers)
print("after ", count)

# submission of the list
# using loops
'''
'''
sum = 0
for numbers in [3, 5, 6, 7, 85, 32, 5, 4, 2]:
    sum = sum + numbers
    print(sum, numbers)
print("got it ")
'''
'''
# Finding the average in a loop
count = 0  # to count the numbers
sum = 0  # for the sum of the numbers
print(count, sum)
for numbers in [2, 4, 5, 7, 8, 6, 5, 4, 3, 223]:
    count = count + 1
    sum = sum + numbers
    print(count, sum)
# print(count,sum)
print("The count is :", count)
print("the sum is :", sum)
print("the average is :", sum / count)


x = [1, 2, 45, 6, 7, 54, ]
print(max(x))  # to find the maximum value in a list

min_numbers = [21, 34, 565, 77, 12, 454, 4454]
print(min(min_numbers))  # to find the minimum number in a list

list = ["banana", 22, 34, 454, "tomato"]
print(len(list))  # to find the length of a list

# Applying some filters in a loop
# for example to print the largest numbers or smallest nnumbers
# by applying conditions

for numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 5, 4, 4, 3, 2, 2]:
    print(numbers)
    if numbers > 5:
        print("the larger numbers are")

print("get the answer")

# String with loop
name = "Neymar"
for letter in name:
    print(letter)

name_1 = "Neymar"
index = 0
while index < len(name_1):
    letter = name_1[index]
    print(index,letter)
    index = index + 1
'''

word = "Hello"
count = 0
for letter in word:
    if letter == "p":
        count = count + 1
        print(count)
    else:
        print("No word found ")


