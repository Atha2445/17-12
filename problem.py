class Student:
    collageName = "IIT"
    def __init__(self,python,web,math):
        self.sub1 = python
        self.sub2 = web
        self.sub3 = math
    def avg(self):
         return ((self.sub1+self.sub2+self.sub3)/3)

    @classmethod
    def collageDetails(cls):
        return cls.collageName 
    @staticmethod
    def staticMethod():
        print("Hello World")    
   



Std1 = Student(4,7,8)        
Std2 = Student(2,3,9) 

print(Std1.avg())
print(Std2.avg())
print(Student.collageDetails())

    
   



