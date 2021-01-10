# Dictionaries and tuples in python
p = "hello"
print(len(p))



names = ['harry', 'ron', 'guy', 'lee']
print("hello", names)
for names in names:
    print("happpy new year ", names)
print(list(names[0]))
print(len(names))
print(list(range(len(names))))

# dictionaries are pythons most powerful data collection
# allow us to do fast database like operations

# count values in a dictionary
# count = 0
count = dict()
names = {'mary', 'mary', 'hello', 'marry', 'tom', 'alex', 'tom'}
for names in names:
    if names not in count:
        count[names] = 1

# tuples can not be changed once declared
# for exampele

x = {1, 'tom', 2, 'jerry', 3, 'duck'}  # a tuple
type(x)
print(x)
print(type(x))

y = [1, 2, 3, 4, 'tom', 'jrry']  # a list
print(type(y))

# dictionary example
# dictionary is a kind of set of list but with no proper address so we have to give  a key to it

name = {'TOM': 'TOM@gmail.com', 'jerry': 'jerry@gamil.com'}
print(name['TOM'])  # it will return the mail of the TOM

for email in name:
    print(name)

# another example is that is
# python unpackaing
players = {'Ronaldo ', 'Messi', 'Kaka'}
realmadrid, Barcelona, Milan = players
print(Milan, Barcelona, realmadrid)

# date and time module

import datetime as dt
import time as tm

print(tm.time())

# map function example
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)  # but it will give a lazy value


list(map(split_title_and_name, people))

# lambda function

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]


# option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# option 2
list(map(split_title_and_name, people)) == list(
    map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))


d = {"apples" : 2, "bananas" : 3, "carrots" : 12}
print(d.get("oranges", 0))
for fruit in d:
    print(fruit)

'''
# problem
# Define a function with the name dict_func that takes one argument (assume string)
# and returns a dictionary with keys as words in the string and
# values as the number of times those words occur in the string.
#
# You can assume that the string will always have at least one word.
#
# Sample Input -
#
# dict_func('the quick brown fox jumps over the lazy dog')
'''
def dict_func(string):
    l = string.split(" ")
    d = dict()
    for word in l:
        if(d.get(word)):
            d[word] += 1
        else:
            d[word] = 1
    return d


print(dict_func("hekko how are you are you ohk ok "))

# working with tuples 
# another simple problems are
t = (12,323, 'd', [1,23], False)
t = (1)
print(type(t))


t1 = tuple("1,2,3,4,5")
t2 = tuple([1,2,3,4,5])
t3 = tuple((1,2,3,4,5))
# enter the number of each elements in the tuples
print(len(t1))
print(len(t2))
print(len(t3))
'''

# tuples
t = (1, 3, 5, 2, 54, 34, 2, 34, 5)
l = len(t)
t = (1, 3, 5, 2, 54, 34, 2, 34, 5)
l = len(t)
print(t[l - 2])  # well the result will be 34
t2 = t[2:5]
print(t2)
t3 = t[1:3] + t2[:]
print(t3)

print((0, 1, 2) < (0, 3))
l = [(0, 23, 34), (2, 34, 23), (1, 34, 23)]
print(l.sort())


# Problem
# Define a function with the name dict_tuple_func that takes a list of integers as an argument.
# It should create a dictionary with the key as the integer and
# the value as the number of times it is present in the list.
# It should return a tuple in which the first element is the dictionary
# (you created above step) and the second element is the sum of all unique integers in the list
# Sample Input -
#
# dict_tuple_func([1, 2, 3, 1, 2, 3])
# Sample Output -
#
# ({1: 2, 2: 2, 3: 2}, 6)


#def dict_tuple_func(list):

