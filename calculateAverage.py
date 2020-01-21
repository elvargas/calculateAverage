# File: calculateAverage.py
# Assignment 5.1
# Eric Vargas
# DESC: This program allows the user to choose from four operations. When an operation is chosen, they're allowed to choose
# two numbers which will be used to calculate the result for the chosen operation. Option 5. will ask the user how
# many numbers they wish to input. This function will use the number of times to run the program within a loop in
# order to calculate the total and average.


# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


# Function to find average of numbers
def average():
    return sum / count


# Function allows the user to run the program until they enter a value which ends the loop.
def cont():
    reply = input("Continue? Y/N ")
    if reply == "n":
        return True


# Main Section
while True:
    # Prompts user to select an operation
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Average")
    # Take input from the user
    select = input("Select an operation: ")

    # Addition
    if select == '1':
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "+", number_2, "=",
              add(number_1, number_2))
    # Subtraction
    elif select == '2':
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "-", number_2, "=",
              subtract(number_1, number_2))
    # Multiply
    elif select == '3':
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "*", number_2, "=",
              multiply(number_1, number_2))
    # Divide
    elif select == '4':
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "/", number_2, "=",
              divide(number_1, number_2))
    # Average
    elif select == "5":
        sum = 0
        count = int(input("How many numbers would you like to enter? "))
        current_count = 0
        while current_count < count:
            print("Number", current_count)
            number = float(input("Enter a number:  "))
            sum = sum + number
            current_count += 1
            # Displays average after last number is entered
            print("The average was:", sum / count)
    else:
        print("Invalid Input")
    if cont():
        break
