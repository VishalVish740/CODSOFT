# Task --> Design a simple calculator with basic arithmetic operations. 
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result of Addition is:", add(num1, num2))
    elif choice == '2':
        print("Result of Substraction is:", subtract(num1, num2))
    elif choice == '3':
        print("Result of Multiplication is:", multiply(num1, num2))
    elif choice == '4':
        print("Result of Division is:", divide(num1, num2))
    else:
        print("Invalid input")

calculator()