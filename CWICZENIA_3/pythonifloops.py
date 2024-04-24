# 1. Write a Python program to find those numbers which are 
# divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
def div_finder():
    for number in range(1500,2701):
        if number % 7 == 0 and number % 5 == 0:
            print(number)
# print(div_finder())

# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

def temp_converter(temp):
    temp = input("Temperature in C or in F? (60C, 45F)")
    degree = int(temp[:-1])
    convertion = temp[-1]
    if convertion.upper() == "C":
        temp = int(round((9*degree) / 5 +32))
        output = "Fahrenheit"
    elif convertion.upper() == "F":
        temp = int(round((degree - 32) * 5 / 9))
        output = "Celsius"
    else:
        print("Input proper temperature")
        quit()
    print("The temperature in ", output, "is", temp, "degrees.")
    return ''
# print(temp_converter(input))

# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. 
# If the user guesses wrong then the prompt appears again until the guess is correct,
#  on successful guess, user will get a "Well guessed!" message, and the program will exit.

def guessing_game(guessed_number):
    import random
    number, guessed_number = random.randint(1,9), 0
    while number != guessed_number:
        guessed_number = int(input('Guess a number between 1 and 9 until you get it right : '))
    print('Well guessed!')
    return ''
# print(guessing_game(input))

# 4. Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def stars():
    n = 5
    for i in range(n):
        print('* ', end="")
        for j in range(i):
             print('* ', end="")
        print('')
    for i in range(n-1, 0, -1):
        for j in range(i):
            print('* ', end="")
        print('')
    return ''
# print(stars())

# 5. Write a Python program that accepts a word from the user and reverses it.
def word_reversed(word):
    word = input('Input a word: ')
    if len(word) > 1:
        word = word[::-1]
    return word
# print(word_reversed(input))

# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

def number_counter():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even_counter = 0
    odd_counter = 0
    for number in numbers:
        if number % 2 == 0:
            odd_counter += 1
        else:
            even_counter += 1
    return 'Even numbers: ', even_counter, ', odd numbers: ', odd_counter
# print(number_counter())

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

def list_printer():
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    for item in datalist:
        print('Type of', item, "is", type(item))
# print(list_printer())

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
def number_printer():
    for number in range(0,6):
        if number == 3 or number == 6:
            continue
        else:
            print(number)
    return ''
# print(number_printer())

# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

def fib_seq():
    x,y = 0,1
    while y < 50:
        print(y)
        x, y = y, x+y
# print(fib_seq())

# 10. Write a Python program that iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
# For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
def fizz_buzz():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print('Buzz')
        else:
            print(i)
    return ''
# print(fizz_buzz())

# 11. Write a Python program that takes two digits m (row) and n (column) 
# as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

def array2d(input, input2):
    row = int(input('Number of rows: '))
    column = int(input2('Number of columns: '))
    array = []
    for i in range(row):
        row = []
        for j in range(column):
            row.append(i * j)
        array.append(row)
    print(array)
# print(array2d(input,input))

# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) 
# as input and prints the lines as output (all characters in lower case).

def line_seq(input):
    lines = []
    while True:
        l = input()
        if l:
            lines.append(l.lower())
        else:
            break
    for l in lines:
        print(l)
    return ''
# print(line_seq(input))


# 13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. 
# The program will print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

def comma_seq(seq):
    numbers = []
    seq = [x for x in input().split(',')]
    for num in seq:
        x = int(num, 2)
        if x % 5 == 0:
            numbers.append(num)
    return numbers
# print(comma_seq(input))


# 14. Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

def digit_calc():
    string = "Python 3.2"
    digits = 0
    letters = 0
    for char in string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        else:
            pass
    return 'Digits: ', digits, 'Letters: ', letters
# print(digit_calc())

# 15. Write a Python program to check the validity of passwords input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

def password_validator(password):
    import re
    password=input('Please input your password: ')

    if(len(password) < 6 or len(password) > 16):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    else:
        print("Valid password")
# print(password_validator(input))


# 16. Write a Python program to find numbers between 100 and 400 (both included) 
# where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

def number_finder():
    numbers = []
    for number in range(100, 401):
        x = str(number)
        if(int(x[0]) % 2 == 0) and (int(x[1]) % 2 == 0) and (int(x[2]) % 2 == 0):
            numbers.append(x)
    return (",".join(numbers))
# print(number_finder())

# 17. Write a Python program to print the alphabet pattern 'A'.
# Expected Output:
#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *

def star_a():
    result = ""
    for row in range(0,7):
        for column in range(0,7):
            if(((column == 1 or column == 5) and row !=0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
                result += "*"
            else:
                result+= " "
        result += "\n"
    return result
# print(star_a())

# 18. Write a Python program to print the alphabet pattern 'D'.
# Expected Output:
#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 
def star_d():
    result = ""
    for row in range(0,7):
        for column in range(0,7):
            if((column == 0 or column == 1 or column == 2 or column == 3) and (row == 0 or row == 6)) or ((column == 0 or column == 4) and row != 0 and row != 6):
                result += "*"
            else:
                result += " "
        result += "\n"
    return result
# print(star_d())

# 19. Write a Python program to print the alphabet pattern 'E'.
# Expected Output:
#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *****

def star_e():
    result = ""
    for row in range(0,7):
        for column in range(0,5):
            if((row == 0 or row == 6) or (row > 0 and row < 3) and column == 0 or (row > 3 and row < 6) and column == 0 or row == 3 and column < 4):
                result +="*"
            else:
                result +=" "
        result += "\n"
    return result
# print(star_e())

# 20. Write a Python program to print the alphabet pattern 'G'.
# Expected Output:
#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

def star_g():
    result = ""
    for row in range(0,7):
        for column in range(0,5):
            if((row == 0 or row == 6) and (column == 1 or column == 2 or column == 3) or 
               (row == 1 or row == 5 or row == 4) and (column == 0 or column == 4) or (row == 2) and 
               (column == 0) or (row == 3) and (column != 1)):
                result += "*"
            else:
                result += " "
        result += "\n"
    return result
print(star_g())