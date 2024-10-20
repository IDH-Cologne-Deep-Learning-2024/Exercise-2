def calc():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Sum: " + add(num1, num2))
    print("Product: " + multiply(num1, num2))

def add(num1, num2):
    sum = str(num1 + num2)
    print(sum)

def multiply(num1, num2):
    product = str(num1 * num2)
    print(product)

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
