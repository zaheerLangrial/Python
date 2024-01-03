
import random

# Python Numbers
# There are three numeric types in Python:

# int
# float
# complex


x = 25 #Int
y = 50.5 #Float
z = 1j #Complex

print(type(x))
print(type(y))
print(type(z))



print('------------------Int-----------------')



                                    # Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 3432232
print(x,type(x))
x = -234232
print(x,type(x))
x = 1
print(x,type(x))


print('------------------Float-----------------')


                                    # Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.


x = 34.32232
print(x,type(x))
x = -234.232
print(x,type(x))
x = float(1)
print(x,type(x))

y = 23.2e100
print(y, type(y))


print('------------------Complex-----------------')

                        # Complex
# Complex numbers are written with a "j" as the imaginary part:


x = 3+5j
y = 5j
z = -5j
print(x , type(x))
print(y , type(y))
print(z, type(z))


print('------------------Complex-----------------')

                    # Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 5 #its int
y = 2.5#its float
z = 10j#its complex

# type Conversion by using int() float() complex()

x = float(5)
y = int(2.5)
z = int(10)


print(x , type(x))
print(y , type(y))
print(z, type(z))


print('------------------Random Number-----------------')


            # Random Number


print(random.randrange(1,10))   