def calc():
    print('select mathematical operator')
    print('adition')
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Sum: " + str(num1+num2))
    print("Product: " + str(num1*num2))

def calcb():
    print('test')

def main():
    print('Run program calc in interactive (i) or in batch (b) mode.')
    choice = str(input())
    if choice == 'i':
        print('running interactive mode')
        calc()
    elif choice == 'b':
        print ('running batch mode')
        calcb()
    else:
        print('no matching input')
        main()
main()