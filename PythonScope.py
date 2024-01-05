

        # Local Scope


def func () : 
    x = 300
    print(x)


func()
# print(x) Error



        # Function Inside Function


# def myFunc () : 
#     x = 'Zaheer'

#     def myInnerFunc () : 
#         print(x) 
#     myInnerFunc()

# myFunc()



        # Global Scope

x = 'Zaheer'
# def myFunc () : 

#     def myInnerFunc () : 
#         print(x) 
#     myInnerFunc()

# myFunc()


    # Naming Variables

def myFunc () : 
    x = 303
    print(x) 

myFunc()
print(x)


        # Global Keyword

def f1 () : 
    global x 
    x = 'Jutt'
    print(x)

f1()
print(x)