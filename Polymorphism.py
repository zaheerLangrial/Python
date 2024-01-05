



        # Class Polymorphism

    # Class One
# class Car : 
#     def __init__ (self , name , mudel):
#         self.name = name
#         self.mudel = mudel
#     def move (self) : 
#         print('Drive')

#     # Class 2nd 
# class Boat :
#     def __init__(self , name , mudal) :
#         self.name = name
#         self.mudel = mudal
#     def move(self) : 
#         print('Sail')

#         # Class 3rd
# class Plane : 
#     def __init__(self , name , mudal) : 
#         self.name = name
#         self.mudel = mudal

#     def move(self) : 
#         print('Sail')

# car1 = Car('Honda' , 2024)
# boat = Boat('Yu' , 2000)
# plane1 = Plane('PIA' , 2020)
# for x in (car1 , boat , plane1) : 
#     x.move()



    # Inheritance Class Polymorphism


class Vahicle : 
    def __init__(self , name , mudel ) :
        self.name = name
        self.mudel = mudel
    def move (self) : 
        print('Move') 

class Car (Vahicle) : 
    pass

class Boat (Vahicle) : 
    def move(self):
        print('Sail')

class Plane (Vahicle) : 
    def move(self):
        print('Fly')

car1 = Car('Honda' , 2024)
boat = Boat('Yu' , 2005)
plane = Plane('PIA' , 2018)

for x in (car1 , boat , plane) : 
    x.move()