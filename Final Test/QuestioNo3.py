

# You are given a positive integer. You can only use one for loop and one print statement. Print a numerical triangle of height like the one below:

            # Input:
            # 5

            # Output:
            # 1
            # 22
            # 333
            # 4444


def QuestionNo3Func (num) : 
    for i in range(num) : 
        if i == 0 : continue
        print(str(i) * i)


QuestionNo3Func(5)