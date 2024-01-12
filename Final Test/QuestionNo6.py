# You get an array of numbers, and return the sum of all of the positive ones. Example [1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. You can not use the if statement.


def sumOfListDigits (list) : 
    return sum(x for x in list if x > 0) 

print(sumOfListDigits([1, -4, 7, 12]))