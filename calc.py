y = 1
while y == 1:
    def batch():
        with open("calculations.txt", "r") as file_object:
            file_read = file_object.read()
            file_object.close()
        file_split = file_read.split("\n")
        #file_sorted = sorted(file_split)
        #print(file_read)
        #print(file_read.split("\n"))
        #print(file_split)
        #print(len(file_split))

        i = len(file_split)-1
        ergebnis = 0
        while i >= 0:
        #print(i)
            jetzt = file_split[i] 
            jetzt_split = jetzt.split(" ")
            #print(jetzt_split)
            if "+" in jetzt:
                #print("add")
                ergebnis += int(jetzt_split[0]) + int(jetzt_split[2])
            if "*" in jetzt:
                #print("mult")
                ergebnis += int(jetzt_split[0]) * int(jetzt_split[2])
            #print(jetzt)
            print(ergebnis)
            ergebnis = 0
            i-=1

    def interactive():
        x=1
        while x == 1:
            print("Which operation would you like to do?")
            print("Enter add for addition or mult for multiplication")
            operation = input()
            def addition():
                print("Enter number 1: ")
                num1 = int(input())
                print("Enter number 2: ")
                num2 = int(input())
                print("Sum: " + str(num1+num2))
            def multiplication():
                print("Enter number 1: ")
                num1 = int(input())
                print("Enter number 2: ")
                num2 = int(input())
                print("Result: " + str(num1*num2))

            if operation == "add":
                addition()
            elif operation == "mult":
                multiplication()
            else:
                print("Not a valid operation")

            print("Do you want to continue doing calculations? Answer yes or no")
            cont = input()
            if cont == "no":
                x+=1

        print("Progeramm ended")

    print("Do you want to run the code in interactive or in batch mode?")

    mode = input()

    if mode == "interactive":
        interactive()
    elif mode == "batch":
        batch()
    else:
        print("Not a valid mode")
    
    print("The programm will automatically continue, enter exit to exit")
    exit = input()
    if exit == "exit":
        y+=1