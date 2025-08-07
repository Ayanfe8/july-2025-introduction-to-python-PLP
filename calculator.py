# Simple Calculator Program

# Ask user for two numbers and an operator
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    # This exit the program if the input is not a number
    exit()

op = input("Enter an operation (+, -, *, /): ")

# Perform the operation based on the input
if op == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif op == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif op == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please use one of: +, -, *, /")
