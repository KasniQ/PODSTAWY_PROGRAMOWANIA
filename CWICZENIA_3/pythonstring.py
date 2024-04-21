# 1. Write a Python program to calculate the length of a string.
def string_length(string):
    number = 0
    for char in string:
        number += 1
    return number
# print (string_length('Ala ma kota'))

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def letter_counter(string):
    counter = 0
    letters = {}
    for i in string:
        keys = letters.keys()
        if i in keys:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
# print (letter_counter("google.com"))

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
#If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def string_cutter(string):
    if len(string) >= 2:
        new_string = string[:2] + '' + string[-2:]
    else:
        new_string = ""
    return new_string
# print(string_cutter("w3resource"))

# 4. Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def char_replacer(string):
    char = string[0]
    string = string.replace(char, "$")
    string = char + string[1:]
    return string
# print(char_replacer("restart"))

# 5. Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def string_maker(string1, string2):
    new_string = string2[:2] + '' +string1[2] + " " + string1[:2] + '' + string2[2]
    return new_string
# print(string_maker("abc","xyz"))

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
def string_changer(string):
    if len(string) >= 3:
        if string[-3:] == "ing":
            string += "ly"
        else:
            string += "ing"
    else:
        string = string
    return string
# print(string_changer("abc"))
# print(string_changer("string"))
# print(string_changer("st"))

# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. 
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'

def poor_deleter(string):
    isnot = string.find("not")
    ispoor = string.find("poor")
    if isnot > 0 and ispoor > 0 and ispoor > isnot:
        string = string.replace(string[isnot:(ispoor+4)], 'good')
        return string
    else:
        return string
# print(poor_deleter("The lyrics is not that poor!"))

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def longest_word(words):
    word_length = []
    for i in words:
        word_length.append((len(i), i))
    word_length.sort()
    return word_length[-1]
# print(longest_word(['Exercises', 'asdjklhfakjsdhfaksdjhf', 'Pythonik', 'Polskagura']))

# 9. Write a Python program to remove the nth index character from a nonempty string.

def char_remover(string, index):
    if len(string) > 0:
        string1 = string[:index]
        string2= string[index+1:]
        return string1 + '' + string2
    else:
        return ''
# print(char_remover("Python", 3))

# 10. Write a Python program to change a given string to a newly string 
# where the first and last chars have been exchanged.
def string_changer(string):
    char1 = string[0]
    char2 = string[-1]
    new_string = char2 + '' + string[1:-1] + '' + char1
    return new_string
# print(string_changer("Pudzian"))

# 11. Write a Python program to remove characters that have odd index values in a given string.
def odd_chars_remover(string):
    new_string = ""
    for i in range(len(string)):
         if i % 2 == 0:
             new_string = new_string + string[i]
    return new_string
# print(odd_chars_remover("Polska"))

# 12. Write a Python program to count the occurrences of each word in a given sentence.
def word_counter(string):
    how_many = dict()
    words = string.split()
    for i in words:
        if i in how_many:
            how_many[i] += 1
        else:
            how_many[i] = 1
    return how_many
# print(word_counter("Pchła pchłę pchła, pchła przez pchłę płakała, że pchła pchłę pchała."))

# 13. Write a Python script that takes input from the user 
# and displays that input back in upper and lower cases.
def upper_or_lower(user_input):
    user_input = input("Enter your string: ")
    return(user_input.upper(), user_input.lower())
# print(upper_or_lower(input))

# 14. Write a Python program that accepts a comma-separated sequence of words as input 
# and prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

def comma_separator(string):
    string = input("Comma-separated words: ")
    words = [word for word in string.split(",")]
    return(",".join(sorted(list(set(words)))))
# print(comma_separator(input))

# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def html_tags(tag, string):
    return "<%s>%s</%s>" % (tag, string, tag)
# print(html_tags('i', 'Python'))
# print(html_tags('b', 'Python Tutorial'))

# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_in_middle(base,string):
    firstpart, secondpart  = base[:len(base)//2], base[len(base)//2:]
    new_string = firstpart + '' + string + '' + secondpart
    return new_string
# print(insert_in_middle('[[]]', 'Python'))
# print(insert_in_middle('{{}}', 'PHP'))
# print(insert_in_middle('<<>>', 'HTML'))

# 17. Write a Python function to get a string made of 4 copies 
# of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
def copy_ending(string):
    if len(string) >= 2:
        ending = string[-2:]
        new_string = ending*4
    return new_string
# print(copy_ending('Python'))
# print(copy_ending('Exercises'))

# 18. Write a Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt
def first_three(string):
    if len(string) > 3:
        new_string = string[:3]
    else:
        new_string = string
    return new_string
# print(first_three('ipy'))
# print(first_three('python'))

# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
def last_part(string):
    string = string.rsplit('-',1)[0]
    return string
# print(last_part("https://www.w3resource.com/python-exercises"))

# 20. Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_if(string):
    if len(string) % 4 == 0:
        string = string[::-1]
    return string
print(reverse_if('abcd'))
print(reverse_if('abc'))
