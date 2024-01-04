
        # Python Dictionaries

myDict = {
    'name' : 'Zaheer',
    'age' : 22,
    'caste' : 'langrial'
}

print(myDict)
print(myDict['caste'])
print(len(myDict))

myDict['colors'] = ['Black', 'White' , 'Red']
print(myDict)
print(type(myDict))

dict1 = dict(name = 'zaheer' , age = 24 , country = 'Pakisten')
print(dict1)


    # Python - Access Dictionary Items

print(dict1['country'] , myDict['colors'])

# using get()method

getDictValue = dict1.get('country')
print(getDictValue)
print(dict1.keys())

    # Get Values

print(dict1.values())

dict1['age'] = 22
print(dict1['age'])


    # Get Items


print(dict1.items())


    # Checking
dict1['color'] = 'black'

if 'color' in dict1 : 
    print('Yes')
else : 
    print('No')


    # Remove Dictionary Items
# print(dict1)
# # dict1.pop('color')
# dict1.popitem()
# print(dict1)

# del dict1['country'] 
# # dict1.clear()
# print(dict1)


    # Loop Dictionaries


for x in dict1 : 
    print(x)   # is tara se propeties print hungi 

for x in dict1 : 
    print(dict1[x])


for x in dict1.values() : 
    print(x)

for x , y in dict1.items() : 
    print(x , y)


    # Copy Dictionaries


# Copy k liye hm Copy mehtod use karay gy yaa fir dict ka method hi use karay gy ik dict ko copy karne k liye
    

    # Nested Dictionaries


myFamily = {
    'child1' : {
        'name' : 'Zaheer Ahmad',
        'age' : 23,
        'year' : 2002
    },
    'child2' : {
       'name' : 'Shahzaib Ahmad',
        'age' : 22,
        'year' : 2003 
    },
    'child3' : {
       'name' : 'Aman Fatima',
        'age' : 16,
        'year' : 2008 
    },
}

print(myFamily)
print(myFamily['child1']['name'])


