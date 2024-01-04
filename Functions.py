

        # Python Functions

def my_func() : 
    print('Hello World , am Zaheer')


my_func()


def func(fname , lname) : 
    print('Hello' , fname , lname+'.' ,'How are You.')


func('Zaheer' , 'Ahmad')


        # Arguments, *args


def tupleArguFunc(*numbers) :
    print(numbers[3]) 
    sum = 0
    for x in numbers : 
        sum += x
    return sum / len(numbers)

avg = tupleArguFunc(1 , 2, 3, 4, 5, 6, 7)   # Matlab yeh k agr hm ik star lagaty hain to yeh values ko as a tuple ly ga 
print(avg)


def youngChild(*childs) : 
    print('hello my youngest child ' , childs[1])


youngChild('chain' , 'leain' , 'jack')




            # Arguments, **kwargs


def dictFunc (**name) : 
    print('His last name is ' + name['lName'])


dictFunc(fName = 'Zaheer' , lName = 'Jutt') 



            # Default Parameter Value

def introFunc (name , country = 'Pakistan') :   #Country default argument
    print('My Name is ' + name , 'My country name is ' + country)

introFunc('Zaheer Ahmad')



            # The pass Statement


def meWapisAoGa () : 
    pass            # pass se hm funciton ko bana k chor skty hain 





