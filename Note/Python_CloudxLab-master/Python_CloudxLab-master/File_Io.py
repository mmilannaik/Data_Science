#  File IO in python
# file input and output
# file Io Basics

'''
"r" - Open a file for reading
"w" - Open a file for writing
"+" - Used to update a file means read and write both
"x" - creates a file if not exists
"a" - means append to add more content to a file
"t" - text mode used for files which have text data
"b" - binary mode used for file which have binary data

'''
'''
# Lets create a text file with name python.txt
f = open("python.txt")      # here now we opened a file
content = f.read()         # use read() function to read the content of the file
print(content)
f.close()
'''
#  if i want to read this file as a binary file we will use "rb" means read as binary
# lets try this
'''
f = open("python.txt","rb")
content = f.read()
print(content)
f.close()
'''
# we can use read() to read the specific amount of content
# for example
'''
f = open("python.txt","r")
content = f.read(10)    # lets say read 10 space worth of content
print(content)          # it will only read the availablee data after that it will igonre the data 
f.close()
'''
# to read the content of the file line by line
# so lets start
'''
f = open("python.txt")
count = 0
for line in f:
    count = count + 1
    #print(count,line)   # it applies \n by default which creates gapes between the lines so to remove this
    print(count,line,end="")  # worked fine

# another way of readinf a file line byt line is
f = open("python.txt")
print(f.readline()) # we can write .readlines to read all the lines in a single line
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

'''

# read and write in a file
# lets start
# we have already seen how to read in a file
# to write in a file we will use "w"
'''
f = open("python.txt",
         "w")  # the read mode will dlete my existiong content and replace it with new one if we are applying "w on a existing file"
f.write("My favourite Naruto Characters")  # and in new file it will simply add the data 
print(f)
'''

# now what if we want to add content in the existing file
# we use append or "a"
# for example
'''
f = open("python.txt","a")
f.write("Naruto\n")
f.write("Kakashi\n")
f.write("Minato")    # every time we palce enter  it will add content to the file
# and to know how many  chatracters we have added we can use a
# for example
a = f.write("Rock lee")
print(a)    # it will give a output 8 that we have added 8 characters to the file
f.close()

# and to read and write and both we use +
# for example

f = open("python.txt", "r+")
print(f.read())
f.write("this is one the best anime")
f.close()
#
# when to know where is the  file pointer
f = open("python.txt")
print(f.readline())
print(f.read(10))   # to read the first 10 characters of the file or as many as characters as we wish
print(f.tell()) # it tells about the current location of the file pointer


# lets try something new
f = open("Sequence.txt", "r+")
content = f.read()
# to count the occurance of a character in the file
#count = 0
#for seq in content:
#    if seq == "A":
#        count = count + 1
#print(str(count))

seq = content.count("A")
print("The count of A in the file1 is",seq)
seq1 = content.count("T")
print("The count of T in the file1 is",seq)
seq2 = content.count("G")
print("The count of G in the file1 is",seq)
seq3 = content.count("C")
print("The count of C in the file1 is",seq)

# AND TO COUNT THE FREQUENCY OF EACH CHARACTER IN THE FILE IS
content1 = {}
for seq in content:
    if seq in content1:
        content1[seq] += 1
    else:
        content1[seq] = 1

print(content1)

#
f = open("python.txt","r+")
print(f.readline())
print(f.readline())
print(f.seek(0))    # the seek function puts the pointer on the described position like in my case it is 0 that means from where you want to start your file
print(f.readline())
f.close()
'''
# with block in file Input and output
# it is generally using the open function in a statement that means what we do in a file or in a statement will be in a statement
# IT WILL NOT AFFECT THE COMPLETE PROGRAM
# we dont need to use f.close with it when the statement ends the file closes automatically

# for example
with open("python.txt") as f:
    print(f.readlines())  # it reads all the lines in one go




