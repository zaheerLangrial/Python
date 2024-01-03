

myTuple = ('Zaheer' , 'Asad' , 'Shahzaib' , 'Adnan')
print(myTuple)

print(type(myTuple))


print(len(myTuple))


# Create Tuple in One item like this 

tupleYeh = ('Zaheer',)  # Agr me edy vicho colon khatam krda ty fir e string hu jana 
print(type(tupleYeh))

        # Access Tuple Items


studentTuple = ('Zaheer' , 'Ahmad' , 'Jutt' , 'Asad' , 'Akmal' , 'Adnan' , 'Baloch')
print(studentTuple[0])
print(studentTuple[-1])
print(studentTuple[2:5])
print(studentTuple[-5:-1])
print(studentTuple[3:])

for x in studentTuple : 
    if 'jutt' in x.lower() : 
        print('Yes its jion')


    # Python - Update Tuples
        
tupleInList = list(studentTuple)
tupleInList.append('Ejaz')
studentTuple = tuple(tupleInList)
print(studentTuple , type(studentTuple))

y = ('mahar',)
studentTuple += y
print(studentTuple)



        # Python - Unpack Tuples


(stu1 , stu2 , stu3 , *stu4) = studentTuple
print(stu1 , stu2 , stu3 , stu4) 

(stu1 , stu2 , *allStu , stu4) = studentTuple
print(stu1 , stu2 , allStu , stu4)




        # Python - Loop Tuples


for x in studentTuple : 
    print(x)

for x in range(len(studentTuple)) : 
    print(studentTuple[x])


        # Python - Join Tuples
    

tupe1 = (1 , 2, 3, 4, 5) 
tuple2 = ('a', 'b', 'c', 'd' , 'e')
tuple3 = tupe1 + tuple2 
print(tuple3)
print(tuple3 * 2)