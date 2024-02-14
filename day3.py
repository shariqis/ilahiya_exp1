# for i in range(5):
#     print(i)
# else:
#     print('else part',i)  
  
# i=0
# while i<5:
#     print(i)
#     i+=1
# else:
#     print('else part ',i)    


# a=7

# for i in range(2,a):
#     if a%i==0:
#         print('it is not prime')
#         break
# else:
#     print('prime number')    


# a="python"
# b=""

# for i in a:
#     b=b+i
#     print(b)

start= int(input('enter start : '))
end= int(input('enter end : '))

for i in range(start,end+1):  
    
    for j in range(2,i):
        if i%j==0:
            break  
    else:
        print(i)     
    