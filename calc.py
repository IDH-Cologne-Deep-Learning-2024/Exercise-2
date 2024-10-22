import sys
def calc():
    print('select mathematical operator')
    print('addition (+) multiplication (*)')

    operator = str(input())
    if operator == '+':

        print('addition: \n')
        x = num_input()
        add(x[0],x[1])
        print('\ncontinue addition? yes (y)')
        t = str(input())
        if t == 'y':
            x = num_input()
            add(x[0],x[1])
        else: 
            print('stopping operartion')

    elif operator == '*':
        print('muliplication: \n')
        x = num_input()
        mult(x[0],x[1])
        print('\ncontinue muliplication? yes (y)')
        t = str(input())
        if t == 'y':
            x = num_input()
            mult(x[0],x[1])
        else: 
            print('stopping operartion')

    else:
        print('no matching input')
    
    print('\ncontinue mathematical operation with diferent operator? yes (y)')
    t = str(input())
    if t == 'y':
        calc()
    else:
        print('stopping operartion')
        sys.exit()

def calcb():
    f = open('Exercise-2/calculations.txt', 'r')
    f_red = f.read()
    f.close()
    f_split = f_red.split('\n')
    
    for x in f_split:
        x.strip()

        if '+' in x:
            x.replace("'", '')
            i = x.find('+')
            add(int(x[:i]),int(x[i+2:]))

        if '*' in x:
            x.replace("'", '')
            i = x.find('*')
            mult(int(x[:i]),int(x[i+2:]))

    print('Calculations in batch mode completed\n') 
    print('stopping operartion')
    sys.exit()

def add(num1, num2):
    print("Sum: " + str(num1+num2))

def mult(num1, num2):
    print("Product: " + str(num1*num2))

def num_input():
    num_input_array = [0,0]
    print("Enter number 1: ")
    num_input_array[0] = int(input())
    print("Enter number 2: ")
    num_input_array[1] = int(input())
    return num_input_array

def main():
    print('Run program calc in interactive (i) or in batch (b) mode.')
    choice = str(input())
    if choice == 'i':
        print('running interactive mode: \n')
        calc()
    elif choice == 'b':
        print ('running batch mode: \n')
        calcb()
    else:
        print('no matching input')
        main()
main()