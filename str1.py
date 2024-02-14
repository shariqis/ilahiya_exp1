# a="python"
# print(a)
# print(type(a))
# print(a[3])
# print(len(a))
# l=len(a)
# print(a[l-1])
# print(a[-5])
# print(a[8])
# print(a*2)
# a[2]='u'
# print('a'<'b')


# for i in a:
#     print(i)


# for i in range(l):
#     print(a[i])



# var = 'mY Name iS Sredha'
# print(var)
# print(var.capitalize())
# # print(var.lower())
# # print(var.upper())
# # print(var.title())
# # print(var.swapcase())


# #String Comparison functions
#
# var = '5345'
# print(var)
# print(var.islower())
# print(var.isupper())
# print(var.isalpha())
# print(var.isnumeric())
# var='dssf$$42CC3434'
# print(var)
# print(var.isalnum())


# a="abcde"
# b="mnopqr"

# s=a[0]+b[0]
# m=a[len(a)//2]+b[len(a)//2]
# l=a[-1]+b[-1]
# print(s+m+l)


# a="P@#yn26at^&i5ve"

# c=0
# l=0
# u=0
# d=0
# s=0

# for i in a:
#     if i.isalpha():
#         c+=1
#         if i.islower():
#             l+=1
#         else:
#             u+=1
#     elif i.isnumeric():
#         d+=1
#     else:
#         s+=1
        
# print("cahr ",c)                        
# print("upper ",u)                        
# print("lowr ",l)                        
# print("digit ",d)                        
# print("spcl ",s)                        


a="abc"    
b="mnopqr"  # aobncm
b=b[::-1]
print(b)
s=''
la=len(a)
lb=len(b)
if la<lb:
    l=lb
else:
    l=la    
    
for  i in range(l): # 5 ->0,1,2,3,4,
    if i<la:
        s+=a[i]
    if i<lb:            
        s+=b[i]
    print(s)