# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
def dictionary_sort():
    import operator
    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print("Original dictionary: ", d)

    sorted_dict = sorted(d.items(), key = operator.itemgetter(1))

    print("Dictionary in ascending order: ", sorted_dict)

    sorted_dict = dict( sorted( d.items(), key=operator.itemgetter(1), reverse=True))
    print('Dictionary in descending order: ', sorted_dict)
    return ''
# print(dictionary_sort())

# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
def key_adding():
    dict = {0: 10, 1: 20}
    dict.update({2: 30})
    return dict
# print(key_adding())

# 3. Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def dict_concatenation():
    dict1 = {1:10, 2:20}
    dict2 = {3:30, 4:40}
    dict3 = {5:50, 6:60}
    new_dict = {}
    for d in (dict1, dict2, dict3): new_dict.update(d)
    return new_dict
# print(dict_concatenation())

# 4. Write a Python script to check whether a given key already exists in a dictionary.
def key_checker(key):
    dict = {1:10, 2:20, 3:30, 4:40, 5:50}

    if key in dict:
        print("Key extists in this dictionary")
    else:
        print("Key does not exist in this dictionary")
    return ''
# print(key_checker(7))
# print(key_checker(5))

# 5. Write a Python program to iterate over dictionaries using for loops.
def dict_looper():
    dict = {1:10, 2:20, 3:30, 4:40}
    for dict_key, dict_value in dict.items():
        print(dict_key, ':', dict_value)
    return ''
# print(dict_looper())

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def dict_maker(n):
    dict = {}
    n = int(input("Input a number: "))
    for i in range(1, n+1):
        dict[i] = i*i
    return dict
# print(dict_maker(input))

# 7. Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
def dict_maker2():
    dict = {}
    for i in range(1, 16):
        dict[i] = i*i
    return dict
# print(dict_maker2())

# 8. Write a Python script to merge two Python dictionaries.
def dict_merge():
    dict1 = {1:10, 2:20, 3:30}
    dict2 = {4:40, 5:50, 6:60}
    dict1.update(dict2)
    return dict1
# print(dict_merge())

# 9. Write a Python program to iterate over dictionaries using for loops.
def dict_iteration():
    dict = {1:10, 2:20, 3:30}
    for x, y in dict.items():
        print(x, y)
    return ''
# print(dict_iteration())

# 10. Write a Python program to sum all the items in a dictionary.
def dict_sum():
    sum = 0
    dict = {1:10, 2:20, 3:30, 4:40}
    for x, y in dict.items():
        sum += y
    return sum
# print(dict_sum())

# 11. Write a Python program to multiply all the items in a dictionary.
def dict_values_multipier():
    dict = {1:10, 2:20, 3:30}
    multipication = 1
    for key, value in dict.items():
        multipication *= value
    return multipication
# print(dict_values_multipier())

# 12. Write a Python program to remove a key from a dictionary.
def key_remover(n):
    dict = {1:10, 2:20, 3:30, 4:40}
    if n in dict:
        del dict[n]
    return dict
# print(key_remover(3))

# 13. Write a Python program to map two lists into a dictionary.
def dict_mapper():
    keys = [1,2,3]
    values = [10,20,30]
    dictionary = dict(zip(keys, values))
    return dictionary
# print(dict_mapper())

# 14. Write a Python program to sort a given dictionary by key.
def dict_sorting():
    dict = {1:10, 3:30, 5:50, 2:20, 8:80, 6:60}
    for key in sorted(dict):
        print("%s: %s" % (key, dict[key]))
    return ''
# print(dict_sorting())

# 15. Write a Python program to get the maximum and minimum values of a dictionary.
def dict_max_min():
    dict = {6:60, 1:10, 8:80, 2:20}
    dict_max = max(dict.keys(), key=(lambda k: dict[k]))
    dict_min = min(dict.keys(), key=(lambda k: dict[k]))
    print("Max: ",dict[dict_max])
    print("Min: ",dict[dict_min])
    return ''
# print(dict_max_min())

# 16. Write a Python program to get a dictionary from an object's fields.
class dictionaryObject(object):
    def __init__(dictionary):
        dictionary.x = '1'
        dictionary.y = '2'
        dictionary.z = '3'
test = dictionaryObject()
# print(test.__dict__)

# 17. Write a Python program to remove duplicates from the dictionary.
def duplicate_remover():
    dictionary = {1:10, 2:20, 3:30, 4:20, 5:50}
    removing = []
    values = set()
    for key,value in dictionary.items():
        if value in values:
            removing.append(key)
        else:
            values.add(value)
    for key in removing:
        del dictionary[key]
    return dictionary
# print(duplicate_remover())

# 18. Write a Python program to check if a dictionary is empty or not.
def if_empty(dictionary):
    if dictionary == {}:
        return "Empty"
    else:
        return "Not empty"
# print(if_empty({}))
# print(if_empty({1:10,2:20}))

# 19. Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
def values_combiner():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    d3 = {}
    for key in d1.keys() | d2.keys():
        d3[key] = d1.get(key, 0) + d2.get(key, 0)
    return d3
# print(values_combiner())

# 20. Write a Python program to print all distinct values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
def print_distinct():
    d = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
    distinct_values = []
    repeated = []
    for dictionary in d:
        for value in dictionary.values():
            if value not in distinct_values:
                distinct_values.append(value)
            else:
                repeated.append(value)
    return distinct_values
print(print_distinct())