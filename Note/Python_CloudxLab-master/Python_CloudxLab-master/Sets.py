# Sets are also a type of data collection in the python
# they are like list tuples dicitionary
# set only retains unique values

s = set()  # thats how we create set
s.add(2)  # this is how we add values in the set
s.add(3)
print(s)

# lets try another function
s1 = s.union({1, 2, 3, 4, 54})
print(s, s1)  # thats how we add two sets

s2 = ({1.3})
print(s2)

# and to remove value from set

s.remove(2)    # this will remove value 2 from set s 
print(s)