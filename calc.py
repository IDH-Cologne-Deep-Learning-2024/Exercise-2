def start(): 
    print('Run program calc in interactive (i) or in batch (b) mode.')
    choice = str(input())
    if choice == 'i':
        print('running interactive mode')
        calc()
    elif choice == 'b':
        print ('running batch mode')
        batch_mode()
    else:
        print('no matching input')
        start()

def calc():    
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
   
    print("Choose between Addition or Multiplication?")
    operation_input = str(input())      
    operation = operation_input.split() # split function to ignore/delete tabs
    if operation[0] == 'Addition':
        add(num1, num2)
    elif operation[0] == 'Multiplication':
        multi(num1, num2)
    else:
        print('Please enter "Addition" or "Multiplication"!')

    ask_restart()

# function for addition
def add(num1, num2): 
    print("Sum: " + str(num1+num2))

# funtion for multiplication
def multi(num1, num2):
    print("Product: " + str(num1*num2))

# Exiting or starting over
def ask_restart(): 
    restart_dict = {"yes" : True, "Yes" : True, "restart" : True, "Restart" : True, "No" : False, "no" : False, "Exit": False, "exit": False}
    print('Do you want to restart?')
    restart = str(input())
    if restart in restart_dict:
        if restart_dict[restart] == True:
            print('Restarting the program.')
            calc()
        elif restart_dict[restart] == False:
            print('Exiting the program.')
            exit()
    else: 
        print('Invalid Input. Exiting.')
        exit()

# batch mode 
def batch_mode(): 
    with open("calculations.txt", "r") as file_object:
        lines = file_object.readlines()
    
    for line in lines: 
        line = line.strip() 
        
        if "+" in line: 
            num1, num2 = map(int, line.split("+")) # split am Pluszeichen und neue Liste mit zwei int Elementen
            print(line)
            add(num1, num2)
        elif "*" in line: 
            num1, num2 = map(int, line.split("*"))
            print(line)
            multi(num1, num2)
        else: 
            print(f"Invalid operation in line: {line}")

    ask_restart()

start()