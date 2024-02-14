# def add(a,b=6):
#     print(a)
#     print(b)
#     print(a+b)
    
# add(3,4)    

# def details(n,p):
#     print('my name is ',n,'my palce is ',p)
    
# details(p='eklm',n='anu' )  


# def add(*a):
#     # print(a+b)
#     print(a)
    
# add([4,5,7,56,34,23])    
  
  
# no_item=int(input('enter no of items : '))  

# p=[]

# for i in range(no_item):
#     pro=int(input('amount : '))
#     p.append(pro)
# print(p)    

# def total(*a):   #([1,2,3,4],)
#     print(type(a))
#     print(a)
#     s='0'
# #     for i in a:
# #         for j in i:
# #             s+=j
# #     print(s)
    
# # # total([2,5,7]) 
# # # print('...............')
# # total(['a','pp','le'])   


# def details(**name):
#     print(name)
#     print(type(name))
#     # print('name is ',name , 'place is ',place)
    
# # details(name='anu',place="eklm")    


# def sum(s1,s2,s3):
#     s=s1+s2+s3
#     return s
#     # print('sum',s)

# def avg(s,n):
#     print('.......',s)
#     # s=s1+s2+s3
#     a=s/n
#     print('avg',a) 
       
# b=sum(2,3,4) 
# print(b)   
# avg(b,3)    


# def sum(t):
#     t=t+5
#     print(t)
    
# b=7
# sum(b)    


# student = {'Jim': 12, 'Anna': 14, 'Preet': 10} 
# def test(student):
#   new = {'Sam':20, 'Steve':21} 
#   student.update(new) 
#   print("Inside the function", student) 
  
# test(student) 
# print("Outside the function:", student)


# student = {'Jim': 12, 'Anna': 14, 'Preet': 10} 
# def test(student): 
#     student = {'Sam':20, 'Steve':21} 
#     print("Inside the function", student) 
#     # return 
# test(student)
# print("Outside the function:", student)



# recur : can be defined as the process 
# of defininfg something in terms of itself

# ie a fun calls itself directly or indirectly

# def fact(n):
#     if n==1:      
#         return 1
#     else:
#         # print(n*fact(n-1))
#         return n*fact(n-1)   
    
#     # 5*fatc(4)
#     # 5*4*fact(3)
#     # 5*4*3*fact(2)
#     # 5*4*3*2*fact(1)
#     # 5*4*3*2*1
    
    
# f=fact(5)
# print(f)       

# # 5->120
# # 5*4*3*2*1
    


# higher order  : it contains other fun as
# a parameter or return a function
# as a output, ie fun work with another fun
# # can store the func in a variable


# def first(a,b):
#     print('////////////////////////////')
#     def second(c):
#         print('......')
#         print(a,b,c)
#         s=a+b+c
#         print(s)
#         print('====================')    
#     return second

# val=first(2, 5)
# # print(val)
# # val(4)



a=[67,90,23,78,45]
a.insert(2,66)
print(a)