def calc():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Sum: " + str(num1+num2))
    print("Product: " + str(num1*num2))

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

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def interactive_mode():
    while True:
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
        except ValueError:
            print("Invalid input, please enter numeric values.")
            continue

        operation = input("Enter the operation (+ for addition, * for multiplication): ").strip()

        if operation == '+':
            result = add(num1, num2)
            print(f"Sum: {result}")
        elif operation == '*':
            result = multiply(num1, num2)
            print(f"Product: {result}")
        else:
            print("Invalid operation. Please enter either + or *.")
            continue

        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            print("Exiting the calculator.")
            break

def batch_mode(filename='calculations.txt'):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  

                try:
                    num1, operation, num2 = line.split()
                    num1 = float(num1)
                    num2 = float(num2)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
                    continue

                if operation == '+':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif operation == '*':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                else:
                    print(f"Skipping line with invalid operation: {line}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    mode = input("Do you want to run in 'interactive' or 'batch' mode? ").strip().lower()

    if mode == 'interactive':
        interactive_mode()
    elif mode == 'batch':
        filename = input("Enter the batch file name (default is 'calculations.txt'): ").strip()
        if not filename:
            filename = 'calculations.txt'
        batch_mode(filename)
    else:
        print("Invalid mode selected. Please choose either 'interactive' or 'batch'.")

if __name__ == "__main__":
    main()
