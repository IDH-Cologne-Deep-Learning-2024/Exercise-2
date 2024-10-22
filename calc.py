def calc():
    while True:
        # Get user input for two numbers
        print("Enter number 1: ")
        num1 = int(input())
        
        print("Enter number 2: ")
        num2 = int(input())

        # Ask the user for the desired operation (addition or multiplication)
        print("Enter operation (add or multiply): ")
        operation = input().strip().lower()

        # Perform the chosen operation and display the result
        if operation == 'add':
            print("Sum: " + str(num1 + num2))
        elif operation == 'multiply':
            print("Product: " + str(num1 * num2))
        else:
            print("Invalid operation. Please enter 'add' or 'multiply'.")

        # Ask the user if they want to continue
        print("Do you want to continue? (yes or no)")
        continue_choice = input().strip().lower()

        if continue_choice != 'yes':
            break

def batch_mode():
    try:
        with open('calculations.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # Expecting format like: "5 + 7" or "5 * 7"
                parts = line.split()

                if len(parts) != 3:
                    print(f"Invalid format: {line}")
                    continue

                num1 = int(parts[0])
                operator = parts[1]
                num2 = int(parts[2])

                if operator == '+':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif operator == '*':
                    print(f"{num1} * {num2} = {num1 * num2}")
                else:
                    print(f"Invalid operator in line: {line}")
    except FileNotFoundError:
        print("File 'calculations.txt' not found.")

def main():
    print('Run program calc in interactive (i) or in batch (b) mode.')
    choice = input().strip().lower()

    if choice == 'i':
        print('Running interactive mode')
        calc()
    elif choice == 'b':
        print('Running batch mode')
        batch_mode()
    else:
        print('No matching input')

if __name__ == "__main__":
    main()