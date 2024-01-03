

            # Boolean Values


print(10 > 9) 
print(10 > 11)
print(11 == 11)


a = 200 
b = 300

if a > b :
    print('Condition is True.')
else : 
    print('Condition is false')


print(bool('Hello'))

x = 300
y = 'Zaheer'
print(bool(x))
print(bool(y))
print(bool())


# Some False VAlue in bool

print(bool())
print(bool({}))
print(bool(0))
print(bool([]))



def myFunc(): 
    return 0

print('My function ' ,bool(myFunc()))



def myFunction(): 
    return True

if myFunction() :
    print('yes its True.')
else : 
    print('No its False.')
