# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.


def parenthesesChecker (parenthesesString) : 
    openParentheses = 0
    closeParentheses = 0
    for x in parenthesesString : 
        if x in '(' :
            openParentheses += 1
        else : 
            closeParentheses +=1
    
    return openParentheses == closeParentheses

print(parenthesesChecker('(())((()())())'))
