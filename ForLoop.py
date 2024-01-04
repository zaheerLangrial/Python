

        # For Loop

mylist = ['Zaheer' , 'Ahmad' , 'Langrial']

for x in mylist : 
    print('My list Values is ' , x)

myStr = 'Banana'

for x in myStr : 
    print(x)


    # Break Statement

for x in mylist : 
    print(x)
    if x.lower() == 'ahmad' : 
        break


    # The Continue Statement 

for x in mylist : 
    if x == 'Ahmad' : 
        continue
    print( 'contunue' , x)


    # Range Method in Loops

for x in range(0 , 31 , 5) : 
    print(x)


    # Else method in for loop 

for x in range(6) : 
    if x == 3 : break 
    print(x)
else : 
    print('End')

    # Nested For Loops 

list1 = ['Zaheer' , 22 , 'male']
list2 = ['Shahazaib' , 21 , 'male']
for x in list1 : 
    for y in list2 : 
        print(x , y)