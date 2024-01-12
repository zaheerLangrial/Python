# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.


def QuestionNo11Func (arr) : 
    a = 0
    b = 1
    largestLength = 0
    largestLengthWord = ''
    for x in range(len(arr)-2) :
        if len(arr[a]+arr[b]) > largestLength : 
            largestLength = len(arr[a]+arr[b])
            largestLengthWord = arr[a]+arr[b]
        a = a + 1
        b = b + 1
    print(largestLengthWord)



strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
QuestionNo11Func(strarr)


# OUtPUt
# folingtrashy