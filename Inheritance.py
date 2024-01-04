

        # Python Inheritance

class Person : 
    def __init__(self , fName , lName) : 
        self.fname = fName
        self.lname = lName

    def name (self) : 
        print(self.fname , self.lname)

p1 = Person('Zaheer' , 'Ahmad')
p1.name()


class Student(Person) : 
    pass

stu1 = Student('Asad' , 'Jutt')
stu1.name()