

        # Python Sets


mySet = {'Zaheer' , 'Ahmad' , 'Jutt' , True , 10 , 0 , False , 22}
print(mySet)
print(len(mySet))



                # Python - Add Set Items


#  For add new item in Set use Add() method 

mySet.add('Shahazaib')
print(mySet)


# AGr hamne 2 set ko combine karna ha to fir hmay update Method ka use karna huga 

my2ndSet = {True , 'Zaheer' , 55}
mySet.update(my2ndSet)
print(mySet)

                # Add Any Iterable


# Sets me hm koi bi itrable cheez ko add kar skty hain for example lists bi 

list1 = ['zaheer', 44 , 77 , 'asad']
mySet.update(list1)
print(mySet)


        # Python - Join Sets

# union Method 

set1 = {'Zaheer' , True , 33}
set2 = {'Ahmad' , False , 44}
set3 = set1.union(set2)
print(set3)