# operators in python
#
# Python have many operators
# most common of them are arithmatic operator
# like
#  +
#  -
#  *
#  //
#  %
#  **

# there are many more
# like
# assignment operator
# bitwise operator
# boolean operator
# identity operator
# membership operator


# example of arithmatic operator
#

a = 2
b = 2
c = a + b  # arithmatic + operator
print(c)  # more of like mathmatic operators
print(a * b)  # multiplication operator
print(a / b)  # divide operator
print(a // b)  # floor division operator
print(a ** b)  # power operator
print(a % b)  # modulo operator or reminder operator

# assignment operator
x = 1  # here "=" is a assignment operator
# another example
x += 5  # it adds 5 in the variable
print(x)  # we can apply it with other arithmatic operators


# COMPARISION OPERATORS
# TYPES OF COMPARISION OPERATORS

i = 10
print(i == 4)   # the output will be false
                # becasue i = 10 and when == operator compares it gives false
# other examples are
print(i > 5)    # true
print(i < 5)    # false
print(i >= 5)   # true
print(i <= 5)   # false


# logical operators
# true or false operator
# like and or not
# FOR EXAMPLE
# and will applied when both logics and conditions are true
# or operator applied only when one condition matters

# example
a = True
b = False
print(a and a)  # output will be true
print(a and b)  # output will be false
print(a or b)  # OUTPUT WILL BE TRUE
print(a or a)  # output will still be true

# identitiy operator
print(a is b)  # false
print(a is not b)  # true

# membership operator
#
list1 = [11,22,3,3,444,55,6,7]
print(212121 not in list1)       # false because it is not in list
print(11 in list1)      # true because it is in list



