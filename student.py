# class Student :
#     def __init__(self,name,favNo):
#         self.name = name
#         self.favNo = favNo

#     def info(self):
#         print("Name is : ", self.name,  "Favourite no. is : ",self.favNo)

# fr1 = Student("Pratik","7")
# fr2 = Student("Shiv","45")
# fr1.info()
# fr2.info()        


class Player:
    def __init__(self):
        self.name = "Ishan"
        self.jerseyNo = 32

    def compare(self,other):
        if (self.jerseyNo == other.jerseyNo):
            return True
        else:
            return False        

p1 = Player()        
p2 = Player()
p2.jerseyNo = 18
if p1.compare(p2):
    print("Same")
else:
    print("Different")    
print(p1.jerseyNo)
print(p2.jerseyNo)        

    
    
    # def info(self):
    #     print("name","age")
        

#class1 = Student()        
#Student.info(class1)
#class1.info()