def add(num1, num2):
        print("Sum: " + str(num1+num2))

def mul(num1,num2):
        print("Product: " + str(num1*num2))

def calc():
    active = True
    while(active):
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())

        print("Would you like to add(+) or multiply(*) the numbers?")
        question = False
        while (not question):
            answer = input()
            if (answer == "+"):
                question = True
                add(num1, num2)
            elif (answer == "*"):
                question = True
                mul(num1, num2)
            else:
                print("please give a valid anwer of \"+\" for add or \"*\" for multiply")


        print("Do you want to continue? (y/n)")
        given = False
        while (not given):
            answer = input()
            if (answer == "y"):
                given = True
            elif (answer == "n"):
                given = True
                active = False
            else:
                print("please give a valid anwer of \"y\" for yes or \"n\" for no")


def batch():
    with open("calculations.txt", "r") as file:
        for line in file.read().split("\n"):
            op = line.split(" ")
            if (len(op) != 3):
                return
            if (op[1] == "+"):
                print(">>", line)
                add(int(op[0]), int(op[2]))
            elif (op[1] == "*"):
                print(">>", line)
                mul(int(op[0]), int(op[2]))

print('Run program calc in interactive (i) or in batch (b) mode.')
choice = str(input())
if choice == 'i':
    print('running interactive mode')
    calc()
elif choice == 'b':
    print ('running batch mode')
    batch()
else:
    print('no matching input')
    calc.py