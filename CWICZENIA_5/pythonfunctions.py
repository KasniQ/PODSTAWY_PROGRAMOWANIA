import string
import sys

# 1. Write a  Python function to find the maximum of three numbers.

def max_of(x, y, z):
    return max(x,y,z)
# print(max_of(1,6,2))

# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def list_sum():
    list = [8, 2, 3, 0, 7]
    total = 0
    for number in list:
        total += number
    return total
# print(list_sum())

# 3. Write a  Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def list_multiplier():
    list = [8, 2, 3, -1, 7]
    total = 1
    for item in list:
        total *= item
    return total
# print(list_multiplier())

# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def string_reversed():
    string = "1234abcd"
    index = len(string)
    new_string = ''
    while index > 0:
        new_string += string[index - 1]
        index -= 1
    return new_string
# print(string_reversed())

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def factorial_counter(number):
    factorial = 1
    for i in range(1,number+1):
        factorial *= i
    return factorial
# print(factorial_counter(3))

# 6. Write a  Python function to check whether a number falls within a given range.
def number_checker(num):
    if num in range(1,10):
        print("number is in the range")
    else:
        print("number is not in the range")
# print(number_checker(12))

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def letter_counter():
    string = 'The quick Brow Fox'
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            continue
    print("Uppercase characters: ", upper, ". Lowercase characters: ", lower, ".")
# print(letter_counter())

# 8. Write a  Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def dist_lister():
    list = [1,2,3,3,3,3,4,5]
    new_list = []
    for number in list:
        if number not in new_list:
            new_list.append(number)
    return new_list
# print(dist_lister())

# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def isPrime(number):
    factors = 0
    if number > 1 :
        for i in range(1,number+1):
            if number % i == 0:
                factors += 1
        if factors == 2:
            print('Number', number, 'is prime')
        else:
            print('Number', number, 'is not prime')
    return ''
# print(isPrime(3))
# print(isPrime(12))

# 10. Write a  Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even_lister():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = []
    for number in list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list
# print(even_lister())

# 11. Write a  Python function to check whether a number is "Perfect" or not.
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def perfect_number(number):
    if number > 0:
        divisors = []
        divisors_excluding = []
        for i in range(1,number+1):
            if number % i == 0:
                divisors.append(i)
        for i in range(1,number):
           if number % i == 0:
                divisors_excluding.append(i)
        total_divisors = 0
        total_divisors2 = 0
        for divisor in divisors:
            total_divisors += divisor
        for divisors in divisors_excluding:
            total_divisors2 += divisors
        if total_divisors2 == number:
            print("Number", number, "is a perfect number")
        elif total_divisors/2 == number:
            print("Number", number, "is a perfect number")
        else:
            print("Number", number, "is not a perfect number")
    return ''
# print(perfect_number(6))
# print(perfect_number(3))
# print(perfect_number(28))

# 12. Write a  Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome_checker(string):
    start = 0
    end = len(string) - 1
    while end >= start:
        if not string[start] == string[end]:
            return False
        start += 1
        end -= 1
    return True
# print(palindrome_checker('aza'))
# print(palindrome_checker('azaz'))

# 13. Write a  Python function that prints out the first n rows of Pascal's triangle.
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

def pascalTriangle(n):
    row = [1]
    x = [0]
    for i in range(max(n,0)):
        print(row)
        row = [l + r for l, r in zip(row + x, x + row)]
    return n >= 1
# print(pascalTriangle(4))

# 14. Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def isPangram(string, alphabet = string.ascii_lowercase):
    alphabet = set(alphabet)
    string_set = set(string.lower())
    return alphabet <= string_set
# print(isPangram("The quick brown fox jumps over the lazy dog"))
# print(isPangram("The"))

# 15. Write a  Python program that accepts a hyphen-separated sequence of words as input 
# and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def hyphen_separator(string):
    words = [n for n in string.split('-')]
    words.sort()
    return '-'.join(words)
# print(hyphen_separator("green-red-yellow-black-white"))

# 16. Write a  Python function to create and print a list 
# where the values are the squares of numbers between 1 and 30 (both included).

def list_creator():
    list = []
    for i in range(1,31):
        list.append(i*i)
    return list
# print(list_creator())

# 17. Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
def text_decorator():
    def bold(func):
        def wrapper():
            return f"<b>{func()}</b>"
        return wrapper

    def italic(func):
        def wrapper():
            return f"<i>{func()}</i>"
        return wrapper

    def underline(func):
        def wrapper():
            return f"<u>{func()}</u>"
        return wrapper
    @bold
    @italic
    @underline
    def decorated_text():
        return "This is a decorated text."
    return decorated_text()
# print(text_decorator())

# 18. Write a Python program to execute a string containing  Python code.
def code():
    mycode = 'print("helloworld")'
    exec(mycode)
# print(code())

# 19. Write a Python program to access a function inside a function.
def function(number):
    def multiply():
        nonlocal number
        number *= 5
        return number
    return multiply()
# print(function(5))

# 20. Write a  Python program to detect the number of local variables declared in a function.
# Sample Output:
# 3
def local_detector():
    number1 = 1
    number2 = 2
    number3 = 3
    number4 = 4
# print(local_detector.__code__.co_nlocals) 

# 21. Write a Python program that invokes a function after a specified period of time.
# Sample Output:
# Square root after specific miliseconds:
# 4.0
# 10.0
# 158.42979517754858
from time import sleep
import math
def after_time(x, ms, number):
    sleep(ms/1000)
    return x(number)
print(after_time(lambda num: math.sqrt(num), 100, 16))
print(after_time(lambda num: math.sqrt(num), 1000,100))
print(after_time(lambda num: math.sqrt(num), 10000, 2137))