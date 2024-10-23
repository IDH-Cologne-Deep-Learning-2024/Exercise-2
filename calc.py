def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def calc():
    while True:
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        
        print("Choose operation: + for addition, * for multiplication")
        operation = input().strip()
        
        if operation == '+':
            result = add(num1, num2)
            print("Result (Sum): " + str(result))
        elif operation == '*':
            result = multiply(num1, num2)
            print("Result (Product): " + str(result))
        else:
            print("Invalid operation.")
        
        # Ask if the user wants to continue
        print("Do you want to perform another calculation? (yes/no)")
        continue_choice = input().strip().lower()
        if continue_choice != 'yes':
            break

print('Run program calc in interactive (i) or in batch (b) mode.')
choice = str(input())
if choice == 'i':
    print('Running interactive mode')
    calc()
elif choice == 'b':
    print('Running batch mode')
    # You would implement batch processing here
else:
    print('No matching input.')

