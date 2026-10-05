def addition(num1, num2):
    return num1 + num2

def substraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return 'invalid! Try another integer' 
    return num1 / num2

print("**** Choose operations ****")
print("1: Addition")
print("2: Subtraction")
print("3: Division")
print("4: Multiplication")
print("5: Exit")

while True:
    choice = int(input("Enter your choice(1 - 5)\n"))

    if choice == 5:
        print("**Exiting the calculator**")
        print("CASIO")
        print("Good Bye")
        break
    elif choice in (1, 2, 3, 4):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == 1:
            c = addition(num1, num2)
            print(c)
            print("***The addition operation is successful***")
        elif choice == 2:
            c = substraction(num1, num2)
            print(c)
            print("Your subtraction operation is successful")
        elif choice == 3:
            c = division(num1, num2)
            print(c)
            print("Your division operation is successful")
        elif choice == 4:
            c = multiplication(num1, num2)
            print(c)
            print("Your multiplication operation is successful")
    else:
        print("Invalid choice, please select 1-5.")