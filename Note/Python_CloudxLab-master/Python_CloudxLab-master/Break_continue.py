# Break and continue in python
# use to exit a while loop
# lets try a program
'''
for i in range(0, 100):
  #  if 1 == 1 or i == 2 or i == 99:
        #continue
    print(i)


i = 0                    # this becomes a infinite loop
while i < 45:
    print(i+1)
    continue
    i = i + 1

'''

# lets try to mimic an atm
# we have total Rupees 10         # we are taking less quantitiy si it will be easy to check the program

total = 10
trans = int(input("Enter amount here: "))
for i in range(1,11):
    if i > 5:
        break
    print(i)



print("bye")






































