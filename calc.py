while True:
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    searchOp = True
    while searchOp:
        print("Enter operation ('+', 'add', 'addition' or '*', 'multi', 'multiplication'):")
        op = str(input())
        if op in ("+", "add", "addition"):
            searchOp = False
            print("Sum: " + str(num1 + num2))
            print("Go again? Enter 'y'")
            rerun = input()
            if rerun != 'y':
                exit()
        elif op in ("*", "multi", "multiplication"):
            print("Product: " + str(num1*num2))
            searchOp = False
            print("Go again? Enter 'y'")
            rerun = input()
            if rerun != 'y':
                exit()
        else:
            print("No Operator found")
