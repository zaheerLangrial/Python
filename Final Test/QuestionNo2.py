
        # Question No 2 


def QuestionNo2Func (words , n) : 
    print(words)
    wordCount = {}
    finalList = []

    for word in words : 
        if word in wordCount : 
            wordCount[word] += 1
        else : 
            wordCount[word] = 1
             
    for word in wordCount : 
        finalList.append(wordCount[word])
    print(len(finalList))
    print(' '.join(map(str , finalList)))



list1 = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
print('Count' ,QuestionNo2Func(list1 , 4))