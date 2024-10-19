def add_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def interactive_mode():
    while True:
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            operation = input("Enter the operation (+ for addition, * for multiplication): ").strip()

            if operation == "+":
                result = add_numbers(num1, num2)
                print(f"Sum: {result}")
            elif operation == "*":
                result = multiply_numbers(num1, num2)
                print(f"Product: {result}")
            else:
                print("Invalid operation. Please enter '+' for addition or '*' for multiplication.")
                continue

            continue_calculation = input("Do you want to continue? (yes/no): ").strip().lower()
            if continue_calculation not in ["yes", "y"]:
                print("Exiting the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

def batch_mode(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if "+" in line:
                    num1, num2 = map(float, line.split("+"))
                    result = add_numbers(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif "*" in line:
                    num1, num2 = map(float, line.split("*"))
                    result = multiply_numbers(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                else:
                    print(f"Invalid line in file: {line}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    mode = input("Do you want to run the calculator in 'interactive' or 'batch' mode? ").strip().lower()
    
    if mode == "interactive":
        interactive_mode()
    elif mode == "batch":
        file_name = input("Enter the name of the file to read calculations from (e.g., calculations.txt): ").strip()
        batch_mode(file_name)
    else:
        print("Invalid mode selected. Please choose 'interactive' or 'batch'.")

if __name__ == "__main__":
    main()

