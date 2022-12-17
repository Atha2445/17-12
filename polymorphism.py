# print(len("Hello"))
# print(([10,20,30]))

# def add(x,y,z = 0):
#     return x+y+z
# print(add(3,4))
# print(add(3,4,5))

#Create a car class without any variables amd methods
# class Car:
#     pass

class Vehicle:
    def __init__(self,name,milage):
        self.name = name
        self.milage = milage

class Bus(Vehicle):
    pass
obj = Bus("ABC",10)
print(obj.milage,obj.name)
        
    
