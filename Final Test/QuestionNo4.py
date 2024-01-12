

# You are given a string. Suppose a character ‘c’ occurs 4 times in the string. Replace these consecutive occurrences of the character 'c' with (4, c) in the string.





def print_digit_pairs (num) :
    digits = []
    counter = {}
    pairs = []
    if num < 0 : 
        return 'Your enter number is invalid.'
    
    for x in str(num) : 
        digits.append(int(x))

    print(digits)


    for x in digits : 
        if x in counter : 
            counter[x] += 1
        else : 
            counter[x] = 1

    for digit in counter : 
        pairs.append((counter[digit] , digit))

    for pair in pairs : 
        print(pair , end=' ')

print_digit_pairs(1222311)


# Output
# (3, 1) (3, 2) (1, 3)



