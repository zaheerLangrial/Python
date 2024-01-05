

        # Python Inheritance

# class Person : 
#     def __init__(self , fName , lName) : 
#         self.fname = fName
#         self.lname = lName

#     def name (self) : 
#         print(self.fname , self.lname)

# p1 = Person('Zaheer' , 'Ahmad')
# p1.name()


# class Student(Person) : 
#     pass

# stu1 = Student('Asad' , 'Jutt')
# stu1.name()



# Over Ride the perant function

# class Person : 
#     def __init__(self , Name , age , country) :
#         self.name = Name
#         self.age = age
#         self.country = country
    
#     def intro(self) : 
#         print(f"My name is {self.name}. i am {self.age} year old. i am form {self.country}.")

# p1 = Person('Zaheer Ahmad' , 22 , 'Pakistan')
# p1.intro()


# class Student(Person) : 
#     def __init__ (self , Name , age , country) : 
#         Person.__init__(self , Name , age , country)

# p1 = Student('Zaheer' , 22 , 'Pak')
# p1.intro()


    # Super() method in Inheritance

class Boy : 
    def __init__ (self , fName , lName) : 
        self.FirstName = fName
        self.lastName = lName


    def printName (self) : 
        print('My name is',self.FirstName , self.lastName)

    # use super() method instead of perant class name

# class Student(Boy) : 
#     def __init__(self , fName , lName , year): 
#         super().__init__(fName , lName )

#         # Add Properties
#         self.age = 22
#         # self.graduationYear = '2019'
#         self.graduationYear = year

# p1 = Boy('Zaheer' , 'Ahmad')
# p1.printName()
# p1 = Student('zaheer' , 'Ahmad' , 2020)
# p1.printName()

#     # Access Add Properties
# print(p1.graduationYear , p1.age)
        

class Student (Boy) : 
    def __init__ (self , fName , lastName , graduationYear):
        super().__init__(fName , lastName)
        self.graduationYear = graduationYear

    def welcome (self) : 
        print(f'Welcome {self.FirstName} in the Graduation Class {self.graduationYear}.')


p1 = Student('Zaheer' , 'Ahmad' , 2022)
p1.welcome()



            





