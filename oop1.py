# class Humen:
#     legs=2
#     eyes=2
    
#     def __init__(self,n,p):
#         self.name=n
#         print('i am humen my name is ',n,'my place is',p)
    
#     def talking(v):
#         print(v.name,'can talk')
        
 

# anu=Humen("anu thomas",'eklm')
# appu=Humen("Apootan","kollam")
# anu.talking()
# appu.talking()
# # shari=Humen()


# class Student:
#     def __init__(self,n,a,g):
#         self.name=n
#         self.age=a
#         self.grade=g
        
#     def show_details(self):
#         print('name',self.name)    
        
# anu=Student('anuthomas',23,'A+')



# class Student:
#     pass        
    

class Square:
    def __init__(self,a):
        self.side=a
    
    def area(self):
        print('area',self.side**2)
        
    def perimeter(self):
        print('perimeter',4*self.side)        

b=Square(3)        
b.area()
b.perimeter()