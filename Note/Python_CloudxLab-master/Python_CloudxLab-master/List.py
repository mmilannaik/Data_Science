
# List in python are like arrays
# they stores values of different types
# such as string , int , float etc
players = ["Messi", "Ronaldo", "Neymar", "Suarez"]  # this is a simple list
players.append("Inesta")  # the append is use to add a value in the varaible
print(players)  # append adds a value in the end

for players in ["Messi", "Ronaldo", "Neymar", "Suarez"]:  # this will check and print all the values in the list
    print(players)
print("They are the best attackers in football\n"
      "best of the best")

dir(players)

# one more example
# to find the largest number in a list

# largest_number = -1
# print(largest_number)
# for the_num in [11, 43, 56, 665, 23]:
#    if the_num > largest_number:
#        largest_number = the_num
#        print(largest_number, the_num)

# print("gottcha",largest_number)


# max([11, 43, 56, 665, 23])
print("the largest number is", max([11, 43, 56, 665, 23]))  # we can also use max function
# to find the largest value in list
'''

'''
the_stock = -1
for stock in [1,2,3,2,4,7,5,4,6,8,9,6]:
    print(stock)
    if stock > the_stock:
        the_stock = stock
        print(the_stock,stock)
print("you should sell",the_stock,"for maximum profit")


# finding even numbers in a list

list = []
for number in range (1,1000):
    if number % 2 == 0:
        print(number)
        list.append(number)


print(list)

# List problem
# Define a function with the name str_list_func that takes an argument (assume str).
# Interchanges the 1st and last letter of each word in that argument and then return the resulting string.
# i.e. l and g in leaning should be interchanged with each other and rest of the letters in
# that word should remain at their position only (learning will become gearninl)
# Sample Input: 'I am learning Python at CloudxLab'
# Sample Output: 'I ma gearninl nythoP ta bloudxLaC'

def str_list_func(s):
    l = s.split(' ')
    i = 0
    for element in l:
        if len(element) > 1:
            first = element[0]
            last = element[len(element)-1]
            middle = element[1:len(element)-1]
            l[i] = last + middle + first
        i+=1
    return ' '.join(l)
print(str_list_func("hello"))

x = "there are so many dogs here"

print(x.split())