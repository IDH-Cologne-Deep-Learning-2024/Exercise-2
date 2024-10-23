def calc():
    print("Choose Operator: */+")
    operator = input()
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    if operator == "*":
        multiply(num1, num2)
    elif operator == "+":
        add(num1, num2)


def batch():
    with open("calculations.txt", "r") as file_object:
        lines = file_object.readlines()
    for line in lines:
        expression = line.strip()
        result = eval(expression)
        print(result)



def multiply(num1, num2):
    print("Product: " + str(num1 * num2))


def add(num1, num2):
    print("Sum: " + str(num1 + num2))


check = True
while check:
    print('Run program calc in interactive (i) or in batch (b) mode.')
    choice = str(input())
    if choice == 'i':
        print('running interactive mode')
        calc()
    elif choice == 'b':
        print('running batch mode')
        batch()
    else:
        print('no matching input')
    print('Do you want to continue? (y/n) ')
    choice = str(input())
    if choice != 'y':
        check = False
