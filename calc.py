import os
import sys
def add():
    print("Sum: " + str(num1+num2))
def mult():
    print("Product: " + str(num1*num2))
def interactive():
    print("Enter number 1: ")
    global num1
    num1= int(input())
    print("Enter number 2: ")
    global num2 
    num2 = int(input())
    print("What operation do you want to do?")
    op = str(input())
    if op == "Multiply":
        mult()
    elif op == "Add":
        add()
    else:
        print("False input answer 'Multiply' or 'Add'")
        op = str(input())

    print("Do you want to continue? y/n")
    restart = str(input())
    if restart == "y":
        interactive()
    else:
        print("The program will be closed")
def batch():
    results = []
    file = open("calculations.txt", "r")
    content = file.readlines()
    for line in content:
        line = line.strip()
        if '+' in line:
            numbers = line.split('+')
            result = int(numbers[0].strip()) + int(numbers[1].strip())
        elif '*' in line:
            numbers = line.split('*')
            result = int(numbers[0].strip()) * int(numbers[1].strip())
        results.append(result)
    return results

print("Do you want to run the Program in 'Interactive' or 'Batch' mode.")
choose = str(input())
if choose == "Interactive":
    interactive()
elif choose == "Batch":
    print(batch())