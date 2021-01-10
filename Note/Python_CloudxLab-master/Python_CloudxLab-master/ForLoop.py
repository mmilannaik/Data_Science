# for loops in python
# they are also conditional statements

# for example
count = 0
list1 = ["Messi", "Suarez", "Vidal", "Dembele", "Sergio", "Pique"]
# for palyers in list1:
#    count = count + 1
#    print(count, palyers)


# what id there is a lsit in a list so how can we access both items or data
# lets try
'''
season_goals = [["Messi", 50], ["Suarez", 30], ["Vidal", 5], ["Dembele", 17], ["Sergio", 2], ["Pique", 5]]
# for goals in season_goals:
#    print(goals)   # this will print it like a list
# we can  also called unpacking of list 
# the better way to do that is

for palyers, goals in season_goals:
    count = count + 1
    print(count, palyers, goals)
'''

# lets apply above program on dictionary
# data set will be same but converted to dictionary
'''
season_goals = [["Messi", 50], ["Suarez", 30], ["Vidal", 5], ["Dembele", 17], ["Sergio", 2], ["Pique", 5]]

dict1 = dict(season_goals)
print(dict1)    # so it will show it as a dictionary as in key and value format
#

for players , goals in dict1.items():
    if goals > 40:
        print(players, goals )
else:
    print(players,"scored", goals,"goals in 2021")          #

'''
# PROBLEM
# CREATE A LIST WHICH CAN CONSISIT OF ANY DATA TYPE BUT WE HAVE TO PRINT ONLY INT DATA TYPE
# AND THAT SHOULD BE GREATER THAN 6

sample_list = ["Messi",23,1,3,2,3,45,76,"cow","tea",12.21,1.1,6,6.6,6.1,"superman"]

for items in sample_list:
    if str(items).isnumeric() and items > 6:
        print(items)