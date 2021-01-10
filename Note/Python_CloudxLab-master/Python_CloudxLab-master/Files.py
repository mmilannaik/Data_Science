# we will use the open() function to read a file
# open returns a file handle

# lets try
import csv
'''


# printing the field names
print("the field names are :" + ", ".join(fields for fields in fields))

# Printing the first five rows of the table (csv file )
for row in rows[:5]:
    for col in rows:
        print("%10s" % col)
        print("\n")

# files related problem
# Define a function with the name as file_read_func that takes the path of the file as an argument
# (assume it as str format).
# Your code should check whether the file exists or not with the given path.
# If there is no file at the given path, return -1, else return the sum of the lengths of all words in the file.
# Please note that your code should not count "\n" which is the newline character.
# Sample Input file -
#
# This is a sample file for testing for Python course for learners in CloudxLab.
#
# Sample output (which is the sum of the length of all the words)-
#
# 65

def file_read_func(path):
    try:
         with open('Customer.csv') as f:
             content = f.read()
             content = content.replace('\n','')
             list_of_words = content.split('')
             sum = 0
             for word in list_of_words:
                 sum = sum + len(word)
                 return sum
    except:
        return  -1

print(file_read_func('Customer.csv'))


import csv
count = 0
xfile = open("Customer.csv")
for Customer in xfile:
    count = count + 1
    print(count)


# how to read a file in python
count = 0
f = open("Customer.csv",'r')
#print(f.read())
#for Customer in f:
#    count = count+1
#    print(count,f)
# to print or read the first line
print(f.readline())

# how to write in a file

f1 = open('Sequence.txt','w')
f1.write("hello\n This is my sequence file")

f1 = open('Sequence1.txt','r')
print(f1.read())

# opening a picture
f1 = open('Sketchpad.png','rb')  # using b for binary
print(f1.read())

for i in f1:
    f1.write(i)
    print(f1.write('i'))
    


# print all the lines in the file
count = 0
sequence = open('Sequence1.txt')
for line in sequence:
    count = count + 1

    print(count, line )
    
 
count = 0
file = open('Sequence1.txt')
inp = file.read()
print(len(inp))
print(inp[:6885])


# PROBLEM
#
# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

file = input("words.txt")
fh = open("words.txt","r")
for i in fh:
    ly = i.rstrip()
    print(ly.upper())
    
# Problem 2

# Write a program that prompts for a file name,
# then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values
# from each of the lines and compute the average of those values and produce an output
# as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name

fname = input("mbox-short.txt")
fh = open(fname)
count = 0
for line in fh:

    if not line.startswith("X-DSPAM-Confidence:"):
        count = count + 1

        continue

    print(line)
'''
