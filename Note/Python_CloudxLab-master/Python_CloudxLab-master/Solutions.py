# to find the greatest number among three numbers

num1 = int(input("Enter nmuber1 here: "))
num2 = int(input("Enter nmuber2 here: "))
num3 = int(input("Enter nmuber3 here: "))

if num1 > num2 and num1 > num3:
    print("Num1 is largest")
elif num2 > num1 and num2 > num3:
    print("Num2 is largest ")
else:
    print("Num3 is largest")
