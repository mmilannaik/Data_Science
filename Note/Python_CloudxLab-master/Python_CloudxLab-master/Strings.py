# Strings
# a program to find the length of a string
# for example
'''
name = "MESSI"
for i in range(0, 5):
    print(name[i])  # this will return the range of the name
print(len(name))

for num in range(0, 10):  # the range will check the numbers from 0,9
    print(num)


# how to count the each letter of the string

index = 0
name = "RONALDO"
while index < len(name):
    letter = name[index]
    print(index,letter)
    index = index + 1
print("\nCool functions and loops ")


# to count specific letter in the string
# with the help of loop
name = 'Penaldo'
count = 0
for letter in name:
    if letter == 'a':
        count = count + 1
        print(count)


n = "tommy"
print(n[0:])  # the colon will counts all the string based on the location or number we have given to it
# more examples
sentence = "what are you doing tom"
print(sentence)
print(sentence[10:])  # it will count the print the string afer 10th location that means the
# output will be
# "ou doing tom"
# and a before colon means
print(sentence[:3])  # all the values or character before 3
# the output will be
#   "wha"

ord('a')
print(ord('a'))  # the ord is a way to find the ascii value of the characters and the letters or numbers
print(ord('5'))
# help('')  # for the help in the string cases

# the upper case and lower case in strings
name = "penaldo"
print(name.upper())  # it will convert all the letters in the upper case
name_1 = "MESSI"
print(name.lower())  # lower will convert al the letters in the lower case

# dir(name)  # ????
# print(dir(name))  # it will shows the methods

# lets use some of this methods
print("hello how are you ".split())  # it will split up all the words in the sentence

print('$'.join("They  will   do waht    they waaant".split()))  # this will join the words with
# we can use other characters also

name = 'Raghu'  # tell weather a string or word is present in string or not
print('r' in name)  # its a boolean check yes or no or True or False

# program to compare the strings

name = "banana"
# string comparision
if name == 'banana':
    print("ohk its banana")
if name < "banana":
    print("your word", name, "comes before banana")
elif name > "banana":
    print("your word", name, "comes after banana")
else:
    print("ohk banana")

# another example
fruit1 = "apple"
fruit2 = "banana"
print(fruit1 > fruit2)  # the comparision is based upon the ascaii values

# to remove the whiteapaces from the strings

name = "      hello "
print(name.strip())  # the strip function will clear all the spaces from both sides

# and the lstrip() and rstrip() used to remove the spaces from the respective sides
# for example
name = "      hello    "
print(name.rstrip())  # remove spaces from right side

print(name.lstrip())  # remove spaces from the left side

# prefixes function
line = "Today is a great day"
print(line.startswith('T'))  # the output will be True

print(line.startswith('t'))  # if we give 't' the output will be False

print(line.endswith('y')) #this will give weather the end of line is True or False according to given condition

# to locate the special character or letters we use find functon
# for exampple

line1 = "waht are you doing @ bus station "
position = line1.find('@')
print(position)  # the @ is present at the 19th position

# Revision
# Position of the specific character in the strings
fruit = "banana"
print(fruit[-1])


# another program
fruit = "Mango"
index = 0
while index < len(fruit):
    word = fruit[index]
    print(index,word)  # now i will give a condition so that the index will run till the condition not become infinite
    index = index + 1


# other similar programs
index = 0
name = "Fernando"
while index < len(name):
    letter = name[index]
    print(name[:3])  # a infinite loop because of no condition :) :)
'''
# Another example
# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)  