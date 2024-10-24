def calc():
    cont = ""
    while cont != "no":
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        print("Enter operator + or *: ")
        opp = str(input())
        
        if opp == "+":
            print("Sum: " + str(sum(num1, num2)))
        elif opp == "*":
    	    print("Product: " + str(multi(num1, num2)))
        else:
    	    print("Unknown operator, please try again")
        
        print("Do you want to continue? Type 'no' to terminate.")
        cont = str(input())
    	
def sum(num1, num2):
	sum = num1 + num2
	return sum

def multi(num1, num2):
	multi = num1 * num2
	return multi

def batch():
    with open("calculations.txt", "r") as file_object:
        file_read = file_object.read()
        file_split = file_read.split("\n")

    for line in file_split:
        operation = line.split(" ")
        
        if len(operation) > 1:
            num1 = operation[0]
            num2 = operation[2]
            opp = operation[1]
            
            if opp == "+":
                result = int(num1) + int(num2)
            elif opp == "*":
                result = int(num1) * int(num2)
            else:
                result = "undefined"
                
            print(line + " = " + str(result))
        
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
