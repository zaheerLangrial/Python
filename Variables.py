x = 5
x = 'Hello am Zaheer'
print(x)


# Varables

x = str(5)
y = int(10)
z = float(3)

print(x , y , z)


        # Get The types of Function Type

print(type(x))
print(type(z))


x = 55
y = 'Zaheer'

print(type(x))
print(type(y))

print('--------------------')


        # Many Values to Multiple Variables

x , y , z = 'Orange' , 'Apple' , 'Mango' # is Tara bi ik Variable Declare kar skty hain In Pyhton
print(z , y , x)
print(type(x))




print('--------------------')

# One Value to Multiple Variables

x = y = z = 'Mango'

print (x)


print('--------------------')


            # Unpack a Collection

fruits = ['jutt' , '5' , 'Shahzaib']

x , y , z = fruits

print(x , y , z )

print(x + y + z)

print('--------------------')

                # Global Variables

x = 'I am Zaheer Ahmad'

def myFunction() : 
    print(x)

myFunction()


print('--------------------')

def my2ndFunc():
    x = 'Hello'
    print(x)
my2ndFunc()
print(x)

print('--------------------')


        # The global Keyword


def myGlobalFunc() : 
    global x 
    x = 'This is globle Keywork'
    print(x)
myGlobalFunc()
print(x)