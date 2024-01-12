# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.


def QuestionNO10Func (word) : 
    if len(word) % 2 == 0 :
        mid = len(word)//2
        print(word[mid-1:mid+1])
    else : 
        mid = len(word)//2
        print(word[mid])

QuestionNO10Func('Zaheer')
QuestionNO10Func('Ahmad')