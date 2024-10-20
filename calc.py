def addition(num1, num2):
    print("Sum: " + str(num1 + num2))

def multiplication(num1, num2):
    print("Product: " + str(num1 * num2))

def interactive():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter math operation (+/*): ")
    op = input().strip()

    if op == "+":
        addition(num1, num2)
    elif op == "*":
        multiplication(num1, num2)
    else:
        print("Invalid input. Please try again.")
        return interactive()

    print("Do you want to continue (yes/no)?: ")
    decision = str(input())
    if decision == "yes":
        return interactive()
    else:
        return

def batch():
    try:
        with open("calculations.txt", "r") as file_object:
            file_content = file_object.readlines()
            for line in file_content:
                num1, op, num2 = line.strip().split()
                if op == "+":
                    addition(int(num1), int(num2))
                elif op == "*":
                    multiplication(int(num1), int(num2))
                else:
                    print("Invalid line.")
    except FileNotFoundError:
        print("Error: calculations.txt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    user_input = input("Do you want to run the program in interactive or batch mode (int/batch)? ").lower().strip()
    if user_input == "int":
        interactive()
    elif user_input == "batch":
        batch()
    else:
        print("This mode is not avaible!")

main()