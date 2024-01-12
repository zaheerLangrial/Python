# Write a function which will take an integer as input and print each digit in a separate line. You are not allowed to use str or any other method will convert the integer into string.


def print_digits (number) : 
    if number < 0 : 
        print ('Your enter number is lessthen 0.')
    if number == 0 : 
        print ('0')
    while number > 0 : 
        digit = number % 10
        print (digit) 
        number //= 10


print_digits(1101)