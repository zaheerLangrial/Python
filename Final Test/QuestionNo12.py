# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result. Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0). If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def QNo12Func (sentance) : 
    sentanceInArr = sentance.split()
    sortedSentance = sorted(sentanceInArr , key=lambda x: int(''.join(filter(str.isdigit, x))))
    print(' '.join(sortedSentance))



QNo12Func('4of Fo1r pe6ople g3ood th5e the2')