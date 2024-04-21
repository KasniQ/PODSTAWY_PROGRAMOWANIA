# 1. Write a Python program to sum all the items in a list.
def sum_items(list):
    sum = 0
    for item in list:
        sum += item
    return sum
# print(sum_items([1, 2, 3, 4, 5]))

# 2. Write a Python program to multiply all the items in a list.
def multiply_items(list):
    sum = 1
    for item in list:
        sum *= item
    return sum
# print(multiply_items([2, 2, 3]))

# 3. Write a Python program to get the largest number from a list.
def largest_number(list):
    return max(list)
# print(largest_number([12,5,10,19,2]))

# 4. Write a Python program to get the smallest number from a list.
def smallest_number(list):
    return min(list)
# print(smallest_number([10,2,128]))

# 5. Write a Python program to count the number of strings from a given list of strings. 
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def string_counter(list):
    counter = 0
    for string in list:
        if len(string) > 1 and string[0] == string[-1]:
            counter += 1
    return counter
# print(string_counter(['abc', 'xyz', 'aba', '1221']))

# 6. Write a Python program to get a list, 
# sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def tuple_sorting(list):
    def last(n):
        return n[-1]
    return sorted(list, key=last)
# print(tuple_sorting([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 7. Write a Python program to remove duplicates from a list.
def remove_duplicates(list):
    new_list = []
    duplicates = []
    for item in list:
        if item not in duplicates:
            new_list.append(item)
            duplicates.append(item)
    new_list.sort()
    return new_list
# print(remove_duplicates([1,2,4,2,5,2,6,1,1,2,5,6,3,4,]))

# 8. Write a Python program to check if a list is empty or not.
def is_empty(list):
    if list == []:
        print("The list is empty")
    else:
        print("The list is not empty")
    return list
# print(is_empty([]))
# print(is_empty([1,2,3]))

# 9. Write a Python program to clone or copy a list.
def copy_list(list):
    new_list = []
    for x in list:
        new_list.append(x)
    return list, new_list
# print(copy_list([1,58,12,1]))

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def word_finder(n, string):
    longer_words = []
    words = string.split()
    for word in words:
        if(len(word)) > n:
            longer_words.append(word)
    return longer_words
# print(word_finder(3,'Bungee jumping can be really fun'))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def list_checker(list1, list2):
    x = False
    for item1 in list1:
        for item2 in list2:
            if item1==item2:
                x = True
    return x
            
# print(list_checker([1,5,2,6,27,13], [71,25,19,15,5,2]))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def element_remover(list):
    new_list = []
    deleted_elements = []
    index = 0
    for x in list:
        if index == 0 or index == 4 or index == 5:
            deleted_elements.append(x)
        else:
            new_list.append(x)
        index += 1
    return new_list
# print(element_remover(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
def array_3d():
    list = [[['*' for column in range(6)] for column in range(4)]for row in range(2)]
    return list
# print(array_3d())

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
def even_remover(list):
    for number in list:
        if number % 2 == 0:
            list.remove(number)
    return list
# print(even_remover([1,2,3,4,5,6,7,8]))

# 15. Write a Python program to shuffle and print a specified list.
def list_shuffle(list):
    from random import shuffle
    shuffle(list)
    return list
# print(list_shuffle([1,2,3,4,5,6,7,8,9]))

# 16. Write a Python program to generate and print a list of the first 
# and last 5 elements where the values are square numbers between 1 and 30 (both included).
def list_generator():
    list = []
    for i in range(1,31):
        list.append(i**2)
    return list[:5], list[-5:]
# print(list_generator())

# 18. Write a Python program to generate all permutations of a list in Python.
def list_permutations():
    import itertools
    return list(itertools.permutations([1,2,3]))
# print(list_permutations())

# 19. Write a Python program to calculate the difference between the two lists.
def difference_calculator(list1, list2):
    diff1 = list(set(list1) - set(list2))
    diff2 = list(set(list2) - set(list1))
    total_difference = diff1 + diff2
    return total_difference
print(difference_calculator([1,2,3,4,5], [1,2,3,4,6]))
# 20. Write a Python program to access the index of a list.
def index_receiver(list):
    for index, value in enumerate(list):
        print(index,value)
# print(index_receiver([1,2,3,4,5]))

# 21. Write a Python program to convert a list of characters into a string.
def string_maker(list):
    string = ''.join(list)
    return string
# print(string_maker(['p', 'i', 'e', 's']))