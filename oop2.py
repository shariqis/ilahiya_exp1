# class Meat_Masala:
#     def __init__(self,n):
#         self.name=n
#         print(self.name,'created')
        
#     def ingredients(self):
#         return 'chilli, pepper,salt' 
    
#     def __del__(self):
#         print(self.name,'lost.............')
    
# sara=Meat_Masala('sara')
# v=sara.ingredients()       
# print(v)
# del sara
# bb=sara.ingredients()
# print(bb)
# # kitchen=Meat_Masala('kitchen')



# class Humen:
#     # def __init__(self):
#     #     print('iam humen')
    
#     def talking(self):
#         print('can talk')   
        
# class Student(Humen):
#     def __init__(self):
#         print('iam student')   
    
#     def study(self):
#         print('can study')          
        
# anu=Student()
# anu.study()
# anu.talking()
# print('...................')
# kiran=Humen()
# kiran.talking()
        
        
class Father:
    def __init__(self):
        print('i am father')
    def work(self):
        print('can work')
        
class Mother:
    # def __init__(self):
    #     print('i am mother')
    
    def multitasking(self):
        print('super mom')    
        
class Child(Mother,Father):
    # def __init__(self):
    #     print('i am child')   
    
    def study(self):
        print('study')         
                
                
anu=Child()
anu.multitasking()          
anu.study()          
anu.work()          