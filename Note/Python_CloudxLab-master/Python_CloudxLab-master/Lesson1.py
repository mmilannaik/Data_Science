# try and except
# program 1
# also called as error handling
try:
    passCode = int(input("Enter passcode here\n"))
except:
    print("Please enter a valid passCode, this is your last chance")
    passCode = int(input("Enter passcode here\n"))


# another exampel is

print("write your name here ")
try:
    name = input()
    if name == "tom":
        print("name matched")
except:
    print("do again please ")


