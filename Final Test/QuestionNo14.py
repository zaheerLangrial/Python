# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]



def unique_in_orderFunc (string) :
    resultArr = []
    strInList = list(string)
    for word in strInList : 
        if not resultArr or word != resultArr[-1] : 
            resultArr.append(word)
    print(resultArr)


unique_in_orderFunc('AAAABBBCCDAABBB')