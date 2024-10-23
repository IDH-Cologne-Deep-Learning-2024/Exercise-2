# import for removing user confirmation on start and choices
import msvcrt
# for linux which I cant test
# import termios
# import tty

def redo():
    print("Press + for a new calculation or any other key to exit.")
    op = msvcrt.getch().decode('utf-8')
    
    if op == '+':
        print("Starting new calculation...")
        run() 
    else:
        print("Exiting the calculator now!")

def run():
    print('Available modes: [i]nteractive and [b]atch.')
    op = msvcrt.getch().decode('utf-8')
    if op == 'i':
        print('entering interactive mode')
        calc()
    elif op == 'b':
        print ('entering batch mode')
        batch()
    else:
        print('Which mode [i] or [b] do you want to start?')

def add():
    print("Sum: " + str(num1+num2))
def mul():
    print("Product: " + str(num1*num2))

    

def calc():
    print("Enter number 1: ")
    global num1
    num1= int(input())
    print("Enter number 2: ")
    global num2 
    num2 = int(input())
    print("What operation(+ or *) do you want to do?")
    op = str(input())
    if op == "+":
        add()
        redo()
    elif op == "*":
        mul()   
        redo()     
    else:
        print("Incorrect query. Please enter any operator(+, or *)")
        op = str(input())

# needs some work, since always unaware of calculations.txt  
def batch():
    try:
        with open("calculations.txt", "r") as file_object:
            file_content = file_object.readlines()
            for line in file_content:
                num1, op, num2 = line.strip().split()
                num1, num2 = int(num1), int(num2)
                if op == "+":
                    add(num1, num2)
                elif op == "*":
                    mul(num1, num2)
                else:
                    print("Incorrect query.")
            redo()
    except FileNotFoundError:
        print("Error: calculations.txt not found.")
        redo()        

redo()        
