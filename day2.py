# a=1
# while a<5:
    
#     # if a==3:
#     #     break
    
#     if a==3:       
#         continue
#     print(a)
#     a+=1
    
# else:
#     print(',,,,,,,,,,,,,,,,,,',a)
# print('complt')    

# a=int(input('enter element : '))
# i=2
# if a>1:
#     while i<a:
#         if a%i==0:
#             print('its not prime')
#             break
#         i+=1
#     else:
#         print('its is prime')    
# else:
#     print('1 is not considered')        

# print('hai', end="00")
# print('welcome')
# print('mmm')

a=0
b=1
c=0
n=15
i=0
print(a,end=' , ')
print(b,end=' , ')

while i<n-2:
    c=a+b
    print(c, end=' , ')
    a=b
    b=c
    i+=1
    