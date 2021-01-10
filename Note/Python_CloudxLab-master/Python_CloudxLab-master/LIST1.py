# List in python
# list in python are the storage of data in python
# list can be mioxed means we can add different different data in the list like str and int together and so on
# it is like array in other programming language
# for example
'''
list1 = [1, 23, 4, 5, 6, 7]  # it is a lsit of the 5 values stored in data set list list1
print(list1)

# lets do a another program related to it
for i in list1:
    print(i)  # this will show all of the list data in the sequence

# lets apply different different functions on the list


# for example .append function
# this will add the any value or data at the -1 position of the list
var = list1.append("tom")
print(list1)

# lets use another function
# .add function

list1[2] = "tommy"    # this will add the data at the desired position
print(list1)

# another one
# remove function removes the desired data from the list
list1.remove("tommy")
print(list1)

# another one
# .copy  function
list1 = [1, 23, 4, 5, 6, 7]
list1.copy()
print(list1)

# another function
# .clear function

list1.clear()
print(list1)  # clears the list, all the data in the list will we vanished or cleared
'''

# lets create a new list

list1 = ["messi", 10, 20, "tiom"]
for i in list1:
    if i == "messi":
        print("create another list")

# lets creaTE A ANOTHER LIST
# and try some new function

num = [1, 2, 3, 4, 5, 6, 7, 87, 9, 0]
num.reverse()
print(num)
num.sort()  # it will sort all the number or data
num.reverse()  # this will reverse all the numbers
print(num)

print(num.count(22))  # it will count the given data in a list if it is available

num.insert(2, "tom")  # it will insert the value on the given location
print(num)

num.pop()  # it will remove the last value of the list
print(num)

num.remove("tom")
print(num)

# lets use slicing with the list

print(num)
print(num[0])  # prints the 0th value on the list
print(num[3])

print(num[1:4])

print(len(num))  # to check the length of the list

# special in slicing
# if we want to jump numbers or data in a sequence we use

print(num[::2])  # this will print all the data form 2 space or values

# we  can also set a range with it for example
#
print(num[1:5:2])  # so it will take the values form 1 t o5 and and them jump form 2-2 values
