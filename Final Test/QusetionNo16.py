# Complete the solution so that the function will break up camel casing, using a space between words.

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""   =>  ""



def BreakCamelCasing(camalCaseString) : 
    result = ''
    for x in camalCaseString : 
        if x.isupper() : 
            result += ' ' + x
        else : 
            result += x
    return result


print(BreakCamelCasing('camelCasing'))
