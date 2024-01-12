# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def stringReverseFunc (string) : 
    reverseWordArr = []
    stringInArr = string.split()
    # stringInArr.reverse()
    # print(stringInArr)
    for x in stringInArr :
        xInArr = list(x)
        xInArr.reverse()
        # print(xInArr) 
        xInArrInstr = ''.join(xInArr)
        reverseWordArr.append(xInArrInstr)
    print(' '.join(reverseWordArr))




stringReverseFunc('A Quick Brown fox for jump over the lazy dog.')