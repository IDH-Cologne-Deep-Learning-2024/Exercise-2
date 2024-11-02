def batch():
    with open("calculations.txt", "r") as file_object:
        file_read = file_object.readlines()
    file_input = file_read#.split("\n")
    print(file_input)
    for term in file_input:
        sep_term = term.split(" ")
        sep_term_left = int(sep_term[0])
        sep_term_right = int(sep_term[-1])
        if "+" in sep_term:
            print(f"Das Ergebnis von {term} ist: {sep_term_left + sep_term_right}")
        elif "*" in term:
            print(f"Das Ergebnis von {term} ist: {sep_term_left * sep_term_right}")

def interactive():
    condition = True
    while condition:

        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        print("Enter operation (add or mul): ")
        op = input()

        def addition(int_1, int_2):
            return int_1 + int_2

        def multiplication(int_3, int_4):
            return int_3 * int_4
        if op == "add":
            print(f"Ergebnis: '{addition(num1, num2)}'")
        elif op == "mul":
            print(f"Ergebnis: '{multiplication(num1, num2)}'")
        else:
            print("You didn't type 'add' for addition or 'mul' for multiplication")
        print("If you want to continue, type 'y'.")
        cont = input()
        if cont == "y":
            print("The program will start again.")
        else:
            condition = False


print("Do you want to run this program in interactive or in batch mode? Type 'interactive' or 'batch'.")
run_mode = input()
if run_mode == "interactive":
    interactive()
elif run_mode == "batch":
    batch()
else:
    print("You didn't type 'interactive' or 'batch'.")