# 1. Write a  Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def dividingByZero():
    try:
        number1 = int(input("Tell me a number you want to divide: "))
        number2 = int(input("Tell me a number you want to divide by:"))
        result = number1/number2
        print(result)
    except ZeroDivisionError:
        print("You can't divide by zero")
# dividingByZero()

# 2. Write a Python program that prompts the user to input 
# an integer and raises a ValueError exception if the input is not a valid integer.
def valueError(prompt="Please enter an integer: "):
    user_input = input(prompt)
    try:
        # Try to convert the input to an integer
        value = int(user_input)
        print(f"You entered the integer: {value}")
        return value
    except ValueError:
        # Raise a ValueError if the input is not a valid integer
        raise ValueError(f"Invalid input: '{user_input}' is not a valid integer")

# if __name__ == "__main__":
#     try:
#         valueError()
#     except ValueError as e:
#         print(e)

# 3. Write a  Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def fileFinder(name):
    try:
        file = open(name, 'r')
        contents = file.read
        print("Content:")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("File does not exist")
# fileFinder("folder")

# 4. Write a Python program that prompts the user to input 
# two numbers and raises a TypeError exception if the inputs are not numerical.
def getInput(prompt):
    user_input = input(prompt)
    try:
        value = float(user_input)
        return value
    except ValueError:
        raise TypeError(f'{user_input} is not a number')

# if __name__ == "__main__":
#     try:
#         num1 = getInput("First number:: ")
#         num2 = getInput("Second number: ")
#     except TypeError as e:
#         print(e)


# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

def fileOpener(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except PermissionError:
        print(f'Permission denied')
        raise 
# fileOpener("plik.txt")

# 6. Write a  Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def rangeError():
    myList = [1,2,3,4,5,6,7]
    index = int(input("Number:"))
    try:
        number = myList[index]
    except IndexError:
        print("Number not in range")
# rangeError()

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
def userCancel():
    try:
        number = int(input("Give me a number:"))
        print(number)
    except KeyboardInterrupt:
        print("Input has been cancelled by user")
# userCancel()

# 8. Write a  Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def arithmeticError(number1, number2):
    try:
        result = number1/number2
        print(f'{number1} divided by {number2} gives: {result}')
    except ArithmeticError:
        print("Arithmetic error occured!")
# arithmeticError(50,10)

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
def read_file(file_name, encoding='utf-8'):
    try:
        with open(file_name, 'r', encoding=encoding) as file:
            content = file.read()
            print(content)
    except UnicodeDecodeError:
        print(f"An UnicodeDecodeError appeared!")
# read_file("example.txt")

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
def attributeError():
    numbers = [1,2,3,4,5,6,7,8,9,0,100,20,3]
    try:
        r = len(numbers)
        print(f'Length of the list: {r}')
    except AttributeError:
        print("An attribute error occured")
# attributeError()
def attributeError2():
    numbers = [1,2,3,4,5,6,7,8,9,0,100,20,3]
    try:
        r = numbers.length
        print(f'Length of the list: {r}')
    except AttributeError:
        print("An attribute error occured")
# attributeError2()