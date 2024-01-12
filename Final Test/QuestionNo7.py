# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ). You can not use the if statement.

def QuestionNo8Func (input) : 
    sorted_arr = sorted(input)
    return sum(sorted_arr[1 : -1])

print(QuestionNo8Func([1,2,3,4,5]))