# 1. Write a  Python program to import a built-in array module and display the namespace of the said module.
# import array
# for namespace in array.__dict__:
#     print(namespace)
# ----------------------------------------------------------------------------------------------------------
# 2. Write a Python program to create a class and display the namespace of that class.
class display:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
# for namespace in display.__dict__:
    # print(namespace)

# ----------------------------------------------------------------------------------------------------------
# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class Npc:
    def __init__(self, npc_id, npc_name, npc_group):
        self.npc_id = npc_id
        self.npc_name = npc_name
        self.npc_group = npc_group
npc=Npc('1','Marcin', '5')
# print(npc.__dict__)

# ----------------------------------------------------------------------------------------------------------
# 4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
# Write a Python program that imports the abs() function using the builtins module, 
# displays the documentation of the abs() function and finds the absolute value of -155.
import builtins
# help(builtins.abs)
# print(builtins.abs(-155))

# ----------------------------------------------------------------------------------------------------------
# 5. Define a  Python function student(). Using function attributes display the names of all arguments.
def student(student_id, student_name, student_class):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'
# print(student('17','Marcin',"III"))

# ----------------------------------------------------------------------------------------------------------
# 6. Write a  Python function student_data () that will print the ID of a student (student_id). 
# If the user passes an argument student_name or student_class the function will print the student name and class.
def student_data(student_id, **args):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in args:
        print(f"Student Name: $ {args['student_name']}")
    if 'student_class' in args:
        print(f"Student Class: $ {args['student_class']}")
# print(student_data(student_id='1', student_name='Marcin'))
# print(student_data(student_id='15152', student_name='Maja', student_class='I'))

# ----------------------------------------------------------------------------------------------------------
# 7. Write a simple Python class named Student and display its type. 
# Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
class Student:
    pass  
# print(type(Student))
# print(Student.__dict__.keys())
# print(Student.__module__)


# ----------------------------------------------------------------------------------------------------------
# 8. Write a Python program to create two empty classes, Student and Marks. 
# Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not.
class Student:
    pass
class Marks:
    pass
studencik = Student()
mark = Marks()
# print(isinstance(studencik, Student))
# print(isinstance(mark, Student))
# print(isinstance(mark, Marks)) 
# print(isinstance(studencik, Marks))
# print("\nIs built=in class?")
# print(issubclass(Student, object))
# print(issubclass(Marks, object)) 

# ----------------------------------------------------------------------------------------------------------
# 9. Write a  Python class named Student with two attributes student_name, marks. 
# Modify the attribute values of the said class and print the original and modified values of the said attributes.
class Student:
    name = 'Marcin'
    grades = 2184721
# print(f"Student Name: {getattr(Student, 'name')}")
# print(f"Grades: {getattr(Student,'grades')}")
# setattr(Student, 'name', 'Maja')
# setattr(Student, 'grades', '3')
# print(f"Student Name: {getattr(Student, 'name')}")
# print(f"Grades: {getattr(Student,'grades')}")

# ----------------------------------------------------------------------------------------------------------
# 10. Write a  Python class named Student with two attributes student_id, student_name. 
# Add a new attribute student_class and display the entire attribute and the values of the class.
# Now remove the student_name attribute and display the entire attribute with values.
""""
class Student:
    student_id = '1'
    student_name = 'Marcin'  
print("Students: ")
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
print("\n New Students: ")
Student.student_class = 'III'
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
print("\n After removing name: ")
del Student.student_name
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
"""

# ----------------------------------------------------------------------------------------------------------
# 11. Write a Python class named Student with two attributes: student_id, student_name. 
# Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
class Student:
    student_id = '1'
    student_name = 'Marcin'
    student_class = "IIIIIII"
    def show():
        print(f'Student id: {Student.student_id} \n Student name: {Student.student_name} \n Student class: {Student.student_class}')
# Student.show()

# ----------------------------------------------------------------------------------------------------------
# 12. Write a  Python class named Student with two instances student1, student2 and assign values to the instances' attributes. 
# Print all the attributes of the student1, student2 instances with their values in the given format.
"""
class Student:
    student1 = {}
    student2 = {}
student1 = Student()
student2 = Student()
student1.student_id = "1"
student2.student_id = "2"
student1.student_name = "Marcin"
student2.student_name = "Maja"
student1.student_class = "III"
student2.student_class = "IV"
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
"""

# ----------------------------------------------------------------------------------------------------------
# 1. Write a Python class to convert an integer to a Roman numeral.
class converter:
    def int_to_roman(num):
        values = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // values[i]):
                roman_num += symbols[i]
                num -= values[i]
            i+=1
        return roman_num
# print(converter.int_to_roman(1000))
# print(converter.int_to_roman(501))

# ----------------------------------------------------------------------------------------------------------
# 2. Write a Python class to convert a Roman numeral to an integer.
class converter:
    def roman_to_int(str):
        roman_values = {"I": 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for i in range(len(str)):
            if i > 0 and roman_values[str[i]] > roman_values[str[i-1]]:
                number += roman_values[str[i]] - 2 * roman_values[str[i-1]]
            else:
                number += roman_values[str[i]]
        return number
# print(converter.roman_to_int('MM'))
# print(converter.roman_to_int('III'))

# ----------------------------------------------------------------------------------------------------------
# 3. Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
"""
class validator:
    def parenthesesValidator(self, str):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for par in str:
            if par in pchar:
                stack.append(par)
            elif len(stack) == 0 or pchar[stack.pop()] != par:
                return False
        return len(stack) == 0
print(validator().parenthesesValidator("()"))
print(validator().parenthesesValidator("()[]{}"))
print(validator().parenthesesValidator("[)"))
print(validator().parenthesesValidator("({[)]"))
print(validator().parenthesesValidator("{{{"))
"""

# ----------------------------------------------------------------------------------------------------------
# 4. Write a  Python class to get all possible unique subsets from a set of distinct integers.
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class subsets:
    def subsets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

# print(subsets().subsets([4,5,6]))

# ----------------------------------------------------------------------------------------------------------
# 5. Write a  Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# Note: There will be one solution for each input and do not use the same element twice.
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4

class finder:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
# print("index1=%d, index2=%d" % finder().twoSum((10,20,10,40,50,60,70),50))

# ----------------------------------------------------------------------------------------------------------
# 6. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

class sum_to_zero:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

# print(sum_to_zero().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

# ----------------------------------------------------------------------------------------------------------
# 7. Write a  Python class to implement pow(x, n).

class pow:
    def power(self,x, n):
        import math
        if x == 0 or n == 1 or x == 1:
            return x
        if x == -1:
            if n%2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n<0:
            return 1/self.power(x,-n)
        val = self.power(x,n//2)
        if n%2 == 0:
            return val*val
        return val*val*x
# print(pow().power(2,2))
# print(pow().power(2,3))
# print(pow().power(2,4))

# ----------------------------------------------------------------------------------------------------------
# 8. Write a  Python class to reverse a string word by word.
# Input string : 'hello . py'
# Expected Output : '. py hello'

class reverse:
    def reversed(self, s):
        return ' '.join(reversed(s.split()))


# print(reverse().reversed('hello .py'))





# ----------------------------------------------------------------------------------------------------------
# 9. Write a Python class that has two methods: get_String and print_String , 
# get_String accept a string from the user and print_String prints the string in upper case.

"""class String:
    def __init__(self):
        self.string = ""
    def get_String(self):
        self.string = input()
    def print_String(self):
        print(self.string.upper())
string = String()
string.get_String()
string.print_String()
"""




# ----------------------------------------------------------------------------------------------------------
# 10. Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.

class rectangle():
    def __init__(self, a ,b):
        self.a = a
        self.b = b
    def rectangle_area(self):
        return self.a*self.b
new = rectangle(5,7)
# print(new.rectangle_area())



# ----------------------------------------------------------------------------------------------------------
# 11. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.

"""class circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
Circle = circle(4)
print(Circle.area())
print(Circle.perimeter())"""





# ----------------------------------------------------------------------------------------------------------
# 12. Write a  Python program to get the class name of an instance in  Python.

class MyClass:
    def get_class_name(self):
        return self.__class__.__name__
class_name = MyClass()
# print(class_name.get_class_name())




# ----------------------------------------------------------------------------------------------------------
# 1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods 
# like calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, 
# which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. 
# Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))

"""class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    def calculate_emp_salary(self, emp_salary, hours):
        overtime = 0
        if hours > 50:
            overtime = hours - 50
        self.emp_salary = self.emp_salary + (overtime * (self.emp_salary/50))
    def assign_department(self, emp_department):
        self.emp_department = emp_department
    def print_employee_details(self):
        print("\nID: ", self.emp_id)
        print("Name: ", self.emp_name)
        print("Salary: ", self.emp_salary)
        print("Department: ", self.emp_department)
employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

employee1.assign_department("SALES")
employee2.assign_department("SALES")

employee1.calculate_emp_salary(1000000000, 60)

employee1.print_employee_details()
employee2.print_employee_details()"""



# ----------------------------------------------------------------------------------------------------------
# 2. Write a  Python class Restaurant with attributes like menu_items, book_table, 
# and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
# Now add items to the menu.
# Make table reservations.
# Take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.
# Note: Use dictionaries and lists to store the data.
"""
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []
    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price
    def book_tables(self, table_number):
        self.book_table.append(table_number)
    def customer_order(self, table_number, customer_order):
        order = {'table_number': table_number, 'order': customer_order}
        self.customer_orders.append(order)
    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))
    def print_table_reservations(self):
        for table in self.book_table:
            print("Table {}".format(table))
    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))
restaurant = Restaurant()

restaurant.add_item_to_menu("Cheeseburger", 6)
restaurant.add_item_to_menu("Pizza", 25)
restaurant.add_item_to_menu("Hamburger", 25)
restaurant.add_item_to_menu("Spaghetti", 15)
restaurant.add_item_to_menu("Fries", 30)

restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)

restaurant.customer_order(1, "Pizza")
restaurant.customer_order(1, "Hamburger")
restaurant.customer_order(2, "Spaghetti")
restaurant.customer_order(2, "Cheeseburger")

print("\nMenu: ")
restaurant.print_menu_items()
print("\nTable reserved: ")
restaurant.print_table_reservations()
print("\nCustomer orders: ")
restaurant.print_customer_orders()
"""


# ----------------------------------------------------------------------------------------------------------
# 3. Write a  Python class BankAccount with attributes like account_number, 
# balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
"""
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening  = date_of_opening 
        self.customer_name = customer_name
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} added to your account.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn from your account.")
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
    def customer_details(self):
        print("Name:", self.customer_name)
        print(f"Balance: ${self.balance}\n")
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)

customer = BankAccount(2, 15235323, "02-01-1999", "Marcin Kowalski")
print("Customer details: ")
customer.customer_details()
customer.deposit(10000000)
customer.check_balance()
customer.withdraw(25200000)
customer.check_balance()
"""



# ----------------------------------------------------------------------------------------------------------
# 4. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
# Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price.

class Inventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, item_name, stock_count, price):
        self.inventory[item_id] = {"item_name":item_name, "stock_count": stock_count, "price": price}
    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["price"] = price
        else:
            print("Item not found in inventory.")
    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Product name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        else:
            return "Item not found"
inventory = Inventory()
inventory.add_item("1", "Sword", 10, 100)
inventory.add_item("2", "Bow", 50, 500)
print("Item Details: ")
print(inventory.check_item_details("1"))
print(inventory.check_item_details("2"))
print("\n Updating item: ")
inventory.update_item("1", 5, 600)
print(inventory.check_item_details("1"))

