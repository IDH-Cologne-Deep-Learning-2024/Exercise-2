exitvalue = "no"

def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

print("Run Script Interactive or Static? (1: Interactive, 2: Static)")
num4 = int(input())

if(num4 == 1):
    while exitvalue == "no":
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        print("Which operation would you like to perform? (1: Addition, 2: Multiplication)")
        num3 = int(input())

        if(num3 == 1):
            print("Your result is " + str(addition(num1, num2)))
        elif(num3 == 2):
            print("Your result is " + str(multiplication(num1, num2)))
        else:
            print("Invalid input")


        print("Do you want to exit the program? (yes/no)")
        exitvalue = input()

        if(exitvalue == "yes"):
            exit()

else:
    with open("calculations.txt", "r") as file_object:
        file_read = file_object.read()
        file_split = file_read.split("\n")
        file_split.pop(-1)

        for i in file_split:
                result = eval(i)
                print(result)










