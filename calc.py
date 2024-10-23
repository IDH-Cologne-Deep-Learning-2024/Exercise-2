def calc():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter either + for addition or x for multiplication: ")
    choice = str(input())
    if choice  == '+':
      print("Sum: " + str(num1+num2))
    elif choice  == 'x':   
       print("Product: " + str(num1*num2))
    print("Enter y if you want to continue or any other key if you want to exit: ")
    choice2 = str(input())
    if choice2 == 'y':
       calc()

def batch():
    with open("calculations.txt", "r") as file_object:
        lines = file_object.readlines()  
    for line in lines:
        expression = line.strip()  
        result = eval(expression)
        print(result)


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
