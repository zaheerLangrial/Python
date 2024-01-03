

        # String


# Assign String to a Variable

x = 'Hello'
print(x)

print('Hello Am Zaheer')

print('--------------Multiline Strings-------------')

# Kehne ka matlab yeh k agr hamay string multiply line me dena ha to am quites ko 3 bhar type karay gy fir stirng likhy gy

a = ''''Hello am zaheer,
i am form bwn,      
Now am learn python'''
print(a)


print('--------------Strings are Arrays-------------')

# Strings are Arrays

# STring ko bi array ki tara destureture kiya ja skta ha 
x = 'Zaheer Ahmad langrial'
print(x[0])


print('--------------Looping Through a String-------------')

# Looping Through a String


for x in 'Zaheer':
    print(x)


print('--------------String Length-------------')


# String Length

# In js length() method ha , PYTHON  me len ha

x = 'Zaheer Ahmad'
print(len(x))

print('--------------check String-------------')

# Check String

text = 'A Quick brownn fox jumper over the lazy dog.'
print('Quick' in text)


# use If Statement

if 'over' in text : 
    print('Over is in text')



# Python - Slicing Strings
    
# In python slice method is different as compare to js slice method

x = '  Zaheer Ahmad ! '
print(x[:7])


print('--------------Modify String-------------')


            # Python - Modify Strings

# Upper Case
# In python string convert into upper case letter use upper()
print(x.upper()) #For upper Case letter
print(x.lower()) #For lower Case letter
print(x.strip()) #For Remove whiteSpaces
print(x.replace('Z','T')) #For replace letter
print(x.split() , type(x)) #For convert string in list Data Type


print('--------------Concatenate String-------------')

            # Python - String Concatenation

x = 'Zaheer'
y = 'Ahmad'
z = x + " " + y  #ConCatenate the strings
print(z)

print('--------------Python - Format - Strings-------------')

# Python - Format - Strings
animal = 'Fox'
color = 'Brown'
text = 'A Quick {} {} for jump into the lazy dog'
print(text.format(color , animal))
