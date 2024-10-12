# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("Welcome to the Simple Calculator!")

    while True:
        # Take input from the user
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result of addition: {add(num1, num2)}")

            elif choice == '2':
                print(f"The result of subtraction: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"The result of multiplication: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"The result of division: {divide(num1, num2)}")

        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid input. Please try again.")

# Run the calculator
calculator()
