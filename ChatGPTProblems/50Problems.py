import math
import random
import string

# Write a Python program to find the factorial of a number.


factorial = 1
number = 5
for x in range(1 ,number +1): 
    factorial *= x
print(factorial)


# Implement a function to check if a number is prime.

def CheckPrimeNumber (num) : 
    if num % 2 == 0 : 
        print('Yes this is prime number.')
    else :
        print('No this is not a prime number')

CheckPrimeNumber(10)


# Write a program to check if a string is a palindrome.

def CheckPalindrome (string) : 
    reverseStr = ''.join(reversed(string))
    if reverseStr == string :
        print('This sTring is Palidrome')
    else : 
        print('This is Not palindrome.')

CheckPalindrome('bab')

# Create a function to calculate the Fibonacci sequence.

            # No

# Write a program to find the greatest common divisor (GCD) of two numbers.

def FindGCDOfNumbers (a, b) :
    print('GCD' ,math.gcd(a,b))

FindGCDOfNumbers(48 , 18)

# Implement a function to reverse a list.

def ReverseLister (enterList) : 

    enterList.reverse()
    print(enterList)
ReverseLister([1,3,4,5,6])

# Create a program to calculate the square root.

def CalSquareRoot (number) : 
    if number % 2 == 0 : 
        return int(math.sqrt(number))
    else : 
        return 'Invalid Value.'
    
print(CalSquareRoot(64))

# Write a function to count the number of vowels in a string.
print(type('Zaheer'))
def VowelsCounter (string) : 
    vowelCounter = 0
    for x in string.lower() :
        if x == 'e' or x == 'i' or x == 'a' or x == 'o' or x == 'u' in string :
            vowelCounter +=1
    return vowelCounter

# print(VowelsCounter('ZAheer')) 

# Implement a basic calculator with functions for addition, subtraction, multiplication, and division.

# value =  input("Enter the Expersion")
# print(value)


# Create a program to convert Celsius to Fahrenheit and vice versa.
# Write a Python script to check if a given year is a leap year.

def LeapYearChecker (year) :
    if year % 4 == 0 : 
        return f'{year} is a leap year.' 
    else : 
        return f'{year} is not a leap year.'
    
print(LeapYearChecker(2007))

# Implement a function to find the minimum and maximum elements in a list.

def miniAndMaxiChecker (list) : 
    maxinumValue = max(list)
    minimumValue = min(list)
    print('The max value is : ' , maxinumValue) 
    print('The minimum Value is :' , minimumValue)

miniAndMaxiChecker([1, 2, 3,4, 55, 6, 43])

# Write a program to find the sum of digits in a number.

def SumFinder (listForSum) : 
    sum = 0
    for x in listForSum : 
        sum += x
    print(sum)

SumFinder([1,2,3,4,5])

# Create a function to find the area of a triangle given its base and height.
# Implement a simple text-based game using loops and conditional statements.
# Write a Python script to generate a random password.

def passwordGenrator (length = 12) : 
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    print(password)
passwordGenrator()

# Create a program to find the intersection of two lists.

def FindIntersection (list1 , list2) : 
    return list(set(list1) & set(list2))

print(FindIntersection([1,2,3] , [2,3,4]))
# Implement a function to check if a number is even or odd.
                # Done
# Write a program to find the LCM (Least Common Multiple) of two numbers.
# Create a function to remove duplicates from a list.
# Implement a basic file handling program to read and write to a text file.
# Write a Python script to count the occurrences of each word in a given text.
# Implement a program to check if a number is a perfect square.
# Create a function to find the length of the hypotenuse of a right-angled triangle.
# Write a program to find the sum of all prime numbers up to a given number.
# Implement a function to check if a word is an anagram of another word.
# Create a program to calculate the average of a list of numbers.
# Write a Python script to reverse the order of words in a sentence.
# Implement a program to find the power of a number using recursion.
# Create a function to rotate elements in a list to the left or right.
# Write a program to check if a given string contains only digits.
# Implement a basic sorting algorithm (e.g., bubble sort, insertion sort).
# Create a function to convert a decimal number to binary.
# Write a Python script to generate a simple ASCII art.
# Implement a program to calculate the area of a circle given its radius.
# Create a function to find the common elements between two lists.
# Write a program to validate an email address.
# Implement a function to check if a given string is a valid palindrome.
# Create a program to find the sum of the first N natural numbers.
# Write a Python script to download an image from the internet.
# Implement a program to find the median of a list of numbers.
# Create a function to generate a list of prime numbers up to a given limit.
# Write a program to find the ASCII value of a character.
# Implement a simple web scraper using a library like BeautifulSoup.
# Create a function to convert a binary number to decimal.
# Write a Python script to create and manipulate a SQLite database.
# Implement a program to find the roots of a quadratic equation.
# Create a function to calculate the perimeter of a rectangle.
# Write a program to find the factors of a number.
# Implement a simple game using the Pygame library.