#!/usr/bin/env python3

"""
Script to do simple calculations (addition and multiplication)

Usage: $ python calc_solution.py
    In the prompt:
        - Enter "b" or "batch" for batch mode
        - Enter "i" or "interactive" for interactive mode

For batch mode, the file "calculations.txt" needs to exit in the same directory
and must contain a formula of either adding or multiplying two numbers (+ or * sign),
with one formula per line.

For interactive mode, enter the first and second number in succession and afterwards
the operation you want to carry out ("+" or "add" or "addition" OR "*" or "mul" or "multiplication")
"""


def add(n1, n2):
    """Add two numbers"""
    return n1 + n2


def mul(n1, n2):
    """Multiply two numbers"""
    return n1 * n2


def interactive():

    # if False, we will exit the main loop
    cont = True

    # as long as cont is True, we loop
    while cont:
        # Get two numbers from user input
        print("Enter number 1: ")
        # Convert type to int, since the input is str
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        print("Enter operation:")
        # Get operator from user input
        op = input()
        # check wether op is contained in a list of allowed strings
        if op in ["addition", "add", "+"]:
            # Call add function on the two numbers
            print(f"Sum: {add(num1, num2)}")
        # Same for multiplication
        elif op in ["multiplication", "mul", "*"]:
            print(f"Product: {mul(num1, num2)}")
        else:
            # If no input conforms to desired input, print this message and
            # continue
            print(f"Couldn't understand user input '{op}'")

        # Ask user if they want to continue in interactive mode
        cont = input("Continue (Y/N)? ")
        if cont in ["Y", "y", "Yes", "yes"]:
            cont = True
        elif cont in ["N", "n", "No", "no"]:
            cont = False
        else:
            print(f"Couldn't understand user input '{cont}', aborting")
            cont = False


def batch():

    # Read in file
    with open("calculations.txt", "r") as file_object:
        file_read = file_object.read()
    # Iterate over all lines of the file
    for line in file_read.split("\n"):
        # Check which operator occurs in line
        if "+" in line:
            # Split at operator and apply appropriate function to the two parts
            # Note that this doesn't check if there are more operators or
            # numbers in the line
            line = line.split("+")
            print(f"Sum: {add(int(line[0]), int(line[1]))}")
        elif "*" in line:
            line = line.split("*")
            print(f"Product: {mul(int(line[0]), int(line[1]))}")
        else:
            print(f"Line '{line}' is malformed, aborting")


# Get the desired mode from user input and run corresponding function
print("Interactive or Batch mode?")
mode = input()
if mode in ["I", "i", "Interactive", "interactive"]:
    interactive()
elif mode in ["B", "b", "Batch", "batch"]:
    batch()
else:
    print(f"Couldn't understand user input '{mode}', aborting")
