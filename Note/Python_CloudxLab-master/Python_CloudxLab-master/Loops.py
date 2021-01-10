
'''
# for and while loop
# the loop conditions

# A sample program
# program 1
# infinite loop
i = 0
while i < 12:     # this will print an infinite loop
    print("hello")
    print("raghu")
print("ohoho")

'''





print("Hey how are you everyone")

# program 2
# another sample  program
# with break
while True:
    line = input(" >")
    if line == 'done':
        break  # break the loop when condition is met
    print(line)
print("Done ")
'''
# program 3


# sample program
# with continue

while True:
    line = input(" >")
    if line == '#':  # this will continue the loop
        continue  # until the next condition is met
   if line == 'done':
       break
       print(line)

# program 4
#print('completed')
import turtle
while True:
    line = input("Please Enter your name\n ")
    line2 = int(input("Please enter your age\n"))
    line3 = input("Please enter your city ")
    line4 = int(input("Please enter your zip code"))
    if line4 == 302033:
        break
        print("You are from Rajasthan ")
        for steps in range(50):
            turtle.color("green")
            turtle.forward(100)
            turtle.right(90)
print("complete")


# revision
# program 5
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Ohk")
print(n)

# Program 6
# break statements

while True:
    line = input(">")
    if line == "done":   # will run the loop util condition got true
        break
    print(line)

print("Correct input")

# program 8
# lets use the conditional statement with some simple programs
# for example we will use the hours and rate program for rent

try:
    hours = float(input("Please enter hours here: "))
    rate = float(input("Please enter the rent here: "))
    extra_hours = 0
    while True:
        if hours >= 40:
            extra_hours = hours - 40
            hours = 40
            pay = hours * rate + 1.5 * extra_hours
            print(pay)
            break
        print("Not applicable for that rate ")  # it is running a infinite loop if the hours are less then 45 ?????
except:
    print("Please enter the correct values ")
    hours = float(input("Please enter hours here: "))
    rate = float(input("Please enter the rent here: "))
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# nested while loop
# while in a while
# lets try for a random problem
# for example

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

fruit = "banana"
for words in fruit:
    print(words)


#
count = 0
name = "Tommy"
for word in name:
    count = count + 1
    print(word,count)
# :) :) :)

# Practise questions

name_1 = "Jeeeery"
count = 0
for words in name_1:
    if words == "e":
        count = count + 1
        print(count)

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

x = '40'
y = int(x) + 2
print(y)


#x = 'From marquard@uct.ac.za'
#print(x[8])

#x = 'From marquard@uct.ac.za'
#print(x[14:3])

print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data.find())

text = "X-DSPAM-Confidence:    0.8475";
text_float = float(text)
print(text.find([]))


text = "X-DSPAM-Confidence:    0.8475;"

pos = text.find("")
suppo = text.find(";",pos)
host = text[pos+23 : suppo]
print(host)
'''
