

        # Python Lists

a = ['Apple' , 'Orange' , 'Mango' , 2 , False , 'Zaheer']
print('The list of fruit is => ' , a[0] , a[5] , a[2])
print('Fruits length is => ' , len(a) , type(a))


            # Python - Access List Items

a = ['Apple' , 'Orange' , 'Mango' , 2 , False , 'Zaheer']
print(a[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])

print(thislist[:3])

print(thislist[-5:])


if 'apple' in thislist : 
    print('Yes apple is include in this list.')
else : 
    print('No Involved.')


        # Python - Change List Items
    
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1] = 'Amrod'
print(thislist)
for x in thislist : 
    print(x)

thislist[1:3] = ['banana' , 'waterMelon']
print(thislist)

thislist[1:4] = ['cherry']
print(thislist)

# Insert items 

fruits = ['mango' , 'Apple' , 'watermelon']
fruits.insert(2 , 'cheery') #Inset is used to add index value in any given index 
print(fruits)

            # Append Items

# in python append method is use to add index value in the end index.

fruits.append('cheer')
print(fruits)

# append() is a method which is use to add vlue in list at the end index.


                # Insert Method

# insert method is used for add specific index value.ValueError

    # Extend List
# Extend method ka name se hi pata chal raha ha k yeh 2 list ko extend karta ha 
a = ['2' , '3' , 4 , '5']
b = ['7' , '9' , 10]
a.extend(b)
print(a)

thisTuple = ('55' , 56 , '22')
a.extend(thisTuple) #Extend is used to to extend any itrable list like as tuple list dictionaries , sets 
print(a)



            # Python - Remove List Items

people = [2, 3, 4 , 5, '44' , 33,22]
people.remove('44')    # using remove Method for remove index value
print(people)

people.insert(3 , '55')
print(people)

del people[3]    #using del method for remove index value
print(people)

people.pop(4)    # Pop se hm direct index bata k index ko remove kar skty hain
print(people)

# in python if we remove a index value in a list .
# python provide 3 different type of method to remove index value in a list

# remove('remove Value')
# del list[index number]
# pop(index number)
# clear() is used to clear a list


            # Python - Loop Lists

for x in people : 
    print(x)


# using index numbers and range method used
    

for x in range(len(people)): 
    print(x)

[print(x) for x in people]



        # Python - List Comprehension

students = ['Asad' , 'Adnan' , 'Zaheer' , 'Ejaz' , 'Ahsan' , 'Awois']
filterStudent = []
for x in students : 
    if "Zaheer" in x : 
        filterStudent.append(x)
print('filter Students is ' , filterStudent)

filterStudent = [x for x in students if 'Zaheer' in x]
print(filterStudent)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fitlerFruits = [x for x in fruits if x != 'kiwi']
print(fitlerFruits)
newFruits = [x for x in fruits]
print(newFruits)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)



            # Python - Sort Lists

students.sort(key=str.lower)
print(students)
students.sort(reverse=True)
print(students)
students.reverse()
print(students)


    # Python - Copy Lists

mylist = students.copy()   #Copy karne ka ik idea yeh ha ik or ha wo list hi ha 
print(mylist)

mylist = list(mylist)
print(mylist)


            # Python - Join Lists

    # Join Two Lists

w = ['jutt' , 'Zaheer' , 'mughal']
y = ['Asad' , 'Noni' , 'Sufi']

# z = w + y                 # One approch this
# print(z)


# for x in y : 
#     w.append(x)
# print('its loop ' , w)      # This is 2nd approch


w.extend(y)
print('entend use ' , w)



