import os

# Set the working directory to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to handle interactive mode
def interactive_mode():
    while True:
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        
        # Ask for operation
        print("Choose operation: + for addition, * for multiplication")
        operation = input().strip()
        
        # Perform the chosen operation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        else:
            print("Invalid operation")
            continue
        
        print(f"Result: {result}")
        
        # Ask if the user wants to continue
        print("Do you want to perform another calculation? (yes/no)")
        cont = input().strip().lower()
        if cont not in ['yes', 'y']:
            print("Exiting interactive mode.")
            break

# Function to handle batch mode
def batch_mode():
    try:
        with open('calculations.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if '+' in line:
                    num1, num2 = map(int, line.split('+'))
                    result = add(num1, num2)
                    print(f"{line} = {result}")
                elif '*' in line:
                    num1, num2 = map(int, line.split('*'))
                    result = multiply(num1, num2)
                    print(f"{line} = {result}")
                else:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("Error: 'calculations.txt' file not found.")

# Main program logic
def main():
    print('Run program in interactive (i) or batch (b) mode.')
    choice = input().strip().lower()
    
    if choice == 'i':
        print('Running interactive mode.')
        interactive_mode()
    elif choice == 'b':
        print('Running batch mode.')
        batch_mode()
    else:
        print('Invalid input. Exiting.')

if __name__ == "__main__":
    main()
