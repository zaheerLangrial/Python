

        # Create a Class

class myclas : 
    x = 5               # This is Class.

print(myclas) 

p1 = myclas()

print(p1.x) 


# class Person : 
#     def __init__(self, name , age) : 
#         self.name = name
#         self.age = age

#     def __str__ (self) : 
#         return f"{self.name}({self.age})"


# p1 = Person('Zaheer' , 22)
# print(p1)
# print(p1.name)
# print(p1.age) 

# print(Person)
# p1 = Person('jutt' , 22)
# print(p1)




# class Person : 
#     def __init__(self , name , country , gender ) : 
#         self.name = name
#         self.country = country
#         self.gender = gender


#     def __str__ (self) : 
#         return f'My name is {self.name}. I am form {self.country}. My Gender is {self.gender}.'
    

# p1 = Person('Zaheer' , 'Pakistan' , 'Male')
# p1 = Person('Asad' , 'USA' , 'Male')
# print(p1)



        # Object Methods

class Person : 
    def __init__(self , name , age ) :
        self.name = name
        self.age = age
    

    def intro (self) : 
        print(f"My name is {self.name}. My age is {self.age}.")

p1 = Person('Zaheer' , 23)
p1.intro()
p1.age = 40
print(p1.age)
print(p1.name)
p1.intro()

# if we need to delete a obj or obj property

# del p1.age
# del p1
p1.intro()

