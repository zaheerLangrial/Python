

    # Data Types in Python

# The python has multiply data types to handle data.

# str
# Numric
# Sequence types
# Mapping Types
# Set Types
#boolean Types
# Binary Types
# None types

print('------------String-----------')
 
x = 'Zaheer' #is Tara se bi is ko declare kar skty hain

print('1st Method => ' , x)

x = str('Hello am Zaheer')  # Or is taara se bi kar skty hain

print('2nd Mehod => ' , x)

print('In String The Type of x is ' , type(x))


print('------------Numberic Types-----------')

    # 1st Int

x = int(10)
print('Number x is => ' , x)
print('In Int The Type of x is ' , type(x))

# Float Data types

# x = 10.5 is tara krlo ya is float k sath krlo value change huty hi Data types change hu jati hain 
x = float(10.5)
print('Number x is => ' , x)
print('In Int The Type of x is ' , type(x))

    # Complex 

# x = complex(1j)
x = 1j
print('Value of X is => ' , x)
print('In Complex the type of x is ', type(x))


print('------------Sequance Types-----------')

# list
# tuple
# range

                # List 
# List type ko js me arr kehty hain
x = ['name', 'age', 'jutt']
x = list(('Jutt' , 'age' , 'Name')) # is tara se bi kar skty hain declare
print('The Values of x is => ' , x)
print('In List The Types of X is => ' , type(x))

                # tuple
x = ('Apple' , 'Oragne' , 'Mango')
x = tuple(('mango', 'Orange', 'Apple')) # is tara se bi kar skty hain declare
print('The Values of x is => ' , x)
print('In tuple The Types of X is => ' , type(x))

                # Range
x = range(5,10)
print('the value of x is => ', x)


print('------------Mapping Types-----------')

# Dict like a js obj data Type

x = {'age' : 5 , 'name' : 'Zaheer' }

# The another syntax of dict

x = dict(name = 'Zaheer', age = 18)

print(x)

print('My name is ' , x['name'] , 'My age is ' , x['age'])
print('The type of x is => ' , type(x))



print('------------Mapping Types-----------')

        # set

x = {'Zaheer', 'Ahmad' , 'langrial'}
x = set(('zaheer', 'langrial'))
print(x)
print('The type of x is => ' , type(x))


    # frozenset

x = frozenset({'Jutt', 'Zaheer' , 'Ahmad'})
print(x)
print('The data type of x is => ' , type(x))


print('------------Boolean Types-----------')

# Commanly use for true and False

x = True
x = False
print(x)
print('The type of x is => ' , type(x))



print('------------Binary Types-----------')


            # bytes

x = b'Hello','am Zaher',
print(x)

            # bytearray
x = bytearray(9)
print(x)
print(type(x))


            # memoryview

x = memoryview(bytes(10))

print(x , type(x))
