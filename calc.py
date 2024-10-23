def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# interactive
def interactive_mode():
    while True:
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        print("Enter the operation (+ for addition, * for multiplication): ")
        operation = input()

        if operation == '+':
            result = add(num1, num2)
            print("Sum: " + str(result))
        elif operation == '*':
            result = multiply(num1, num2)
            print("Product: " + str(result))
        else:
            print("Invalid operation.")

        # continue?
        print("Do you want to continue? (y/n)")
        cont = input().lower()
        if cont != 'y':
            break
# batch
def batch_mode():
    try:
        with open("calculations.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()  
                if "+" in line:
                    num1, num2 = map(int, line.split('+'))
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif "*" in line:
                    num1, num2 = map(int, line.split('*'))
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                else:
                    print(f"Invalid format in line: {line}")
    except FileNotFoundError:
        print("File 'calculations.txt' not found.")

def run_calculator():
    print('Run program in interactive (i) or batch (b) mode.')
    choice = input().lower()
    if choice == 'i':
        print('Running interactive mode...')
        interactive_mode()
    elif choice == 'b':
        print('Running batch mode...')
        batch_mode()
    else:
        print('Input does not match')

run_calculator()