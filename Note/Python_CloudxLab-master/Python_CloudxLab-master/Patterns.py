# create a star pattern with python programming
# Pattern PRINTING
# TAKE AN INTGER N
# BOOLEAN

print("How many rows you want")
row = int(input())
print("Type 0 or 1")
bool1 = int(input())
new = bool(bool1)
if bool1 == True:
    for i in range(1,row+1):
        for j in range(1, i + 1):
            print("*",end=" ")
        print()
elif bool1 == False:
    for i in range(row,0,-1):
        for j in range(1, i + 1):
            print("*",end=" ")
        print()
