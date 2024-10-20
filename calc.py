def calc():
    active = True
    while(active):
        #user input
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())

        #select method of operation and do the maths thing
        print("Add or multiply? (+/*)")
        ans = str(input())
        if ans == '+':
            add(num1, num2)
        elif ans == '*':
            multiply(num1, num2)
        #imagine..a third option in case of error 

        #confirmation to continue or not
        print("Continue? (y/n)")
        ans = str(input())
        if ans =='y':
            calc()
        elif ans =='n':
            print("Stopping calculator... Bye!")
            active = False

#functions to add and multiply
def add(num1, num2):
    sum = num1 + num2
    print("Sum: "+ (str(sum)))

def multiply(num1, num2):
    product = num1 * num2
    print("Product: "+ (str(product)))

print('Run program calc in interactive (i) or in batch (b) mode.')
choice = str(input())
if choice == 'i':
    print('running interactive mode')
    calc()
elif choice == 'b':
    print ('running batch mode')
else:
    print('no matching input')
    calc.py
