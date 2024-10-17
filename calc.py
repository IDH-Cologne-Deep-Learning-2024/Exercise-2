#Asks for Input, saves that input in three variables. 
# 1.'func1' to determine wether to a addition or multiplikation is wanted
# 2. 'num1' and 'num2' for the two numbers with which the calculation will compute.
# Then the function checks wether "add" or 'multi' was entered and calls on the respective funktion. If neither was 
# enterd the user will be alerted and the function starts again. If a calculation method was choosen, the function 
#'calcRerun' is called to start ask the user to continue. 

def calc():
    print("Enter 'add' for additon or 'multi' for multiplication: ")
    func1=input() 
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    if func1=="add":
        add(num1, num2)
        calcRerun()
    elif func1=="multi":
        multi(num1, num2)
        calcRerun()
    else: 
        print("please only enter 'add' or 'multi'")
        calc()


def calcRerun():  
    print("Do you want to continue? Please enter yes or no: ")
    conti= str(input())
    
    if conti=="yes":
        start()
    elif conti=="no":
        print("Goodbye!")
        exit()
    else:
        print("Please only enter 'yes' or 'no': ")
        calcRerun()

def add(num1, num2): 
    print("Sum: " + str(num1+num2))

def multi(num1, num2):
    print("Produkt: "+str(num1*num2))

#The batch function starts when the user enters 'b' instead of 'i' for the first Input. The function then reads the file 
#calculation.txt and saves it in a variable. This variable is then first split into a list 'splitCalcFile' by linebreaks. A loop iterates over each
#element in the list and splits each element into another list by whitespaces. Then current data splits every element into three elements
# with the element in postion 1 beeing the symbol which determines the funktion, that has to be called. The elements in postion 0 and 2
#contain the numbers which are used in the calcuation. when the loop is over the program starts again. 
    
def batch():
    with open ("calculations.txt", "r") as file_object:
        calcFile=file_object.read()
        splitCalcFile=calcFile.split("\n")

        for element in splitCalcFile: 
            lineContent=element.split(" ")
            if lineContent[1]=="+":
                add(int(lineContent[0]), int(lineContent[2]))
                print("\n")
            elif lineContent[1]=="*":
                multi(int(lineContent[0]), int(lineContent[2]))
                print("\n")
        print("Done!\n")
        calcRerun()

def start():
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


start()