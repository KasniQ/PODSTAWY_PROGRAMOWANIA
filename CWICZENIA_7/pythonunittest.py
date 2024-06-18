# 1. Write a Python unit test program to check if a given number is prime or not.

import unittest


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
# class PrimeNumberTestCase(unittest.TestCase):z
    def test_prime_numbers(self):
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        print("Prime numbers:", prime)
        for number in prime:
            self.assertTrue(isPrime(number), f"{number} is not a prime number")

    def test_non_prime_numbers(self):
        nonPrime = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        print("Non-prime numbers:", nonPrime)
        for number in nonPrime:
            self.assertFalse(isPrime(number), f"{number} is not a prime number")
# if __name__ == '__main__':
#     unittest.main()

# 2. Write a Python unit test program to check if a list is sorted in ascending order.

def ascendingOrderTest(myList):
    return all(myList[i] <= myList[i+1] for i in range(len(myList)-1))

# class ascendingOrderTetser(unittest.TestCase):
    def testList(self):
        myList = [1,2,3,4,5,6,7]
        print("Sorted list: ", myList)
        self.assertTrue(ascendingOrderTest(myList), "List is sorted in ascending order")
    def testWrongList(self):
        myList = [1,5,6,2,4,3]
        print("Unsorted list: ", myList)
        self.assertFalse(ascendingOrderTest(myList), "List is unsorted")
# if __name__ == '__main__':
    # unittest.main()


# 3. Write a Python unit test program that checks if two lists are equal.

def equalLists(list1, list2):
    return list1 == list2

# class testListsEquality(unittest.TestCase):
    def testEqualLists(self):
        print("\nEqual list test:\n", [5,582,37,238], "\n", [5,582,37,238])
        self.assertTrue(equalLists([5,582,37,238], [5,582,37,238]), "The lists are equal")

    def testUnequalLists(self):
        print("\nUnequal list test:\n", [1, 2, 3, 4], "\n", [4,5,6,778435])
        self.assertFalse(equalLists([1, 2, 3, 4], [4,5,6,778435]), "The lists are not equal")

# if __name__ == '__main__':
#     unittest.main()



# 4. Write a Python unit test program to check if a string is a palindrome.

def isPalindrome(s):
    return s == s[::-1]

# class testPalindrome(unittest.TestCase):
    
    def testIfPalindrome(self):
        palindrome = "kajak"
        print('Test palindrome: ', palindrome)
        self.assertTrue(isPalindrome(palindrome), "String is a palindrome")

    def testIfNotPalindrome(self):
       notAPalindrome = "hello"
       print("Testing non palindrome: ", notAPalindrome)
       self.assertFalse(isPalindrome(notAPalindrome), "String is not a palindrome")

# if __name__ == "__main__":
#     unittest.main()



# 5. Write a Python unit test program to check if a file exists in a specified directory.

import os

def file_exists(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

# class TestFileExists(unittest.TestCase):
    
    def test_file_exists(self):
        print("Testing an existing file: ")
        self.assertTrue(file_exists(".", "example.txt"))
    
    def test_file_not_exists(self):
        print("Testing non existent file: ")
        self.assertFalse(file_exists(".", "nonexistent.txt"))

# if __name__ == "__main__":
#     unittest.main()


# 6. Write a Python unit test that checks if a function handles floating-point calculations accurately.


def addFloats(a, b):
    return a + b

# class testFloatingPoint(unittest.TestCase):
    def testAddFloats(self):
        print("Test:", addFloats(0.1, 0.2))
        self.assertAlmostEqual(addFloats(0.1, 0.2), 0.3, places=7)
        print("Test:", addFloats(1.1, 2.2))
        self.assertAlmostEqual(addFloats(1.1, 2.2), 3.3, places=7)

# if __name__ == "__main__":
#     unittest.main()


# 7. Write a Python unit test program to check if a function handles multi-threading correctly.
import threading

def task():
    result = 0
    for i in range(1, 50):
        result += i
    return result

# class multiThreadingTester(unittest.TestCase):
    def testMultiThreading(self):
        numberOfThreads = 10
        threads = []
        for _ in range(numberOfThreads):
            t = threading.Thread(target=task)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        for t in threads:
            self.assertFalse(t.is_alive())
# if __name__ == "__main__":
#     unittest.main()


# 8. Write a Python unit test program to check if a database connection is successful.

import sqlite3

"""class databaseConnectionTester(unittest.TestCase):
    def test_database_connection(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("SELECT 10")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        self.assertEqual(result, (10,))"""
# if __name__ == '__main__':
#     unittest.main()



# 9. Write a Python unit test program to check if a database query returns the expected results.

class testDatabaseQuery(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE friends (id INTEGER PRIMARY KEY, name TEXT, surname TEXT)")
        self.cursor.execute("INSERT INTO friends (name, surname) VALUES ('Marcin', 'Kowalski')")
        self.cursor.execute("INSERT INTO friends (name, surname) VALUES ('Jan', 'Nowak')")
        self.conn.commit()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_database_query(self):
        self.cursor.execute("SELECT name, surname FROM friends ORDER BY name")
        results = self.cursor.fetchall()

        expected_results = [('Jan', 'Nowak'),  ('Marcin', 'Kowalski')]

        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()


# 10. Write a Python unit test program to check if a function correctly parses and validates input data.

"""def parseAndValidate(data):
    if isinstance(data, str) and data.isnumeric():
        return int(data) > 0
    return False

class testInputParsing(unittest.TestCase):
    def test_valid_input(self):
        data = "214892147721841289342178"
        result = parseAndValidate(data)
        self.assertTrue(result)

    def test_invalid_input(self):
        data = "Euro 2024"
        result = parseAndValidate(data)
        self.assertFalse(result)
"""
# if __name__ == '__main__':
#     unittest.main()
