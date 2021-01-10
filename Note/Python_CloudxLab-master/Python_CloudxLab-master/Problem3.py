# Health management system
# we have create a diet and exercise plan for three clients
# need to create different different files for diet and exercise for each client seperately
# that means we should be able to retrive or append the file

# first i will try to solve this problem with simple if else
# then with function

# lets try

client_name = ["TOM", "JERRY", "GOOFY"]
client_name1 = input("Enter client name: ")
action = int(input("write the avction you want to take 1 for read and 2 for write "))
action_type = int(input("Enter 1 for diet 2 for excercise: "))

if client_name1 in client_name and client_name1 == "TOM" and action == 1 and action_type == 1:

    f1 = open("tom_diet.txt")
    content1 = f1.read()
    print(content1)

elif client_name1 in client_name and client_name1 == "TOM" and action == 1 and action_type == 2:
    f1 = open("tom_exercise.txt")
    content1 = f1.read()
    print(content1)

elif client_name1 in client_name and client_name1 == "TOM" and action == 2 and action_type == 1:
    f1 = open("tom_diet.txt", "w")
    content1 = f1.write("")
    print(content1)

elif client_name1 in client_name and client_name1 == "TOM" and action == 2 and action_type == 2:
    f1 = open("tom_exercise.txt", "w")
    #  diet = input()
    content1 = f1.write()
    print(content1)

# for jerry

elif client_name1 in client_name and client_name1 == "JERRY" and action == 1 and action_type == 1:
    f2 = open("jerry_diet.txt")
    content2 = f2.read()
    print(content2)

elif client_name1 in client_name and client_name1 == "JERRY" and action == 1 and action_type == 2:
    f2 = open("jerry_exercise.txt")
    content2 = f2.read()
    print(content2)

elif client_name1 in client_name and client_name1 == "JERRY" and action == 2 and action_type == 1:
    f2 = open("jerry_diet.txt", "w")
    content2 = f2.read()
    print(content2)

elif client_name1 in client_name and client_name1 == "JERRY" and action == 2 and action_type == 2:
    f2 = open("jerry_exercise.txt", "w")
    content2 = f2.read("=")
    print(content2)

# for GOOFY

elif client_name1 in client_name and client_name1 == "GOOFY" and action == 1 and action_type == 1:
    f3 = open("goofy_diet.txt")
    content3 = f3.read()
    print(content3)

elif client_name1 in client_name and client_name1 == "GOOFY" and action == 1 and action_type == 2:
    f3 = open("goofy_exercise.txt")
    content3 = f3.read()
    print(content3)

elif client_name1 in client_name and client_name1 == "GOOFY" and action == 2 and action_type == 1:
    f3 = open("goofy_diet.txt", "w")
    content3 = f3.read("=")
    print(content3)

elif client_name1 in client_name and client_name1 == "GOOFY" and action == 2 and action_type == 2:
    f3 = open("goofy_exercise.txt", "w")
    content3 = f3.read("=")
    print(content3)

else:
    print("Enter names correctely")