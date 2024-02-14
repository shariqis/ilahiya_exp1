# lst4=[1,2,3,4,5,6,7,8,9,0,2,3,-45,6,7,8,2]
# print(lst4)
# # print(lst4.index(2,4,7)) ##gives first index position
# print(lst4.find(2))

# # a=['anu','ammu','kiran','karthik']
# # print(a)
# # a[3]='asif'
# # print(a)
# # a[4]='asif'
# # print(a)
# # a.append('asif')
# # print(a)
# # a.insert(7,'asif')
# # print(a)
# # print(a[4])

# # a=[1,2,3,4,5]
# # b=[6,7,8,9,10]

# # a.extend(b)
# # print(a)
# a=['anu','ammu','kiran','karthik']
# print(a)
# a.extend('anjali')
# print(a)
# # a.append('anjali')
# # print(a)
# a.append([1,2,3])
# print(a)




# ##### remove elements

# vowels = ['a','e','i','o','u']
# print(vowels)
# # vowels[1]=""
# print(vowels)
# del vowels[2]
# print(vowels)

# vowels = ['a','e','i','o','u']
# del vowels[1:3]
# print(vowels)

# vowels = ['a','e','i','o','u']
# del vowels[7]
# print(vowels)

# xyz=['b','c','d','f','g','h','j','b']
# print(xyz)
# n=xyz.remove('b')
# print(xyz)
# print(n)


# consonants=['b','c','d','f','g','h','j']
# consonants.remove('x')
# print(consonants) ## raises ValueError


# consonants=['b','c','d','f','g','h','j']
# print(consonants)
# b=consonants.pop(3)## removes element at specified index
# print(consonants)
# print(b)


# con=['b','c','d','f','g','h','j']
# con.pop() #### removes element at last index
# print(con)


# s=['a','g','adf',2,3,45,67,7]
# print(s)
# s.clear()
# print(s)



# limit=int(input('enter limit : '))
# a=[]
# for i in range(limit):
#     e=int(input('enter element : '))
#     a.append(e)
# print(a)

# l1=['zero','one','two','three','four','five']
# l2=['ten','eleven','twelve','thirteen','fourteen']
# l3=['','','twenty','thirty','fourty','fifty']

# num=int(input('enter number : '))

# if num<10:
#     print(l1[num])
# elif num>=10 and num<20:
#     r=num%10
#     print(l2[r])   
# else:
#     o=num%10
#     t=num//10
#     if o==0:
#         print(l3[t])
#     else:    
#         print(l3[t]+l1[o])    



a=[[1,2,3],[4,5,6],[7,8,9]]    

# for i in a:
#     for j in i:
#         print(j,end=' ') 
#     print()    

# for i in range(3):
#     for j in range(3):
#         print(a[i][j] , end=" ") 
#     print()

# rows=int(input('enter no of rows : '))
# col=int(input('enter no of col : '))
# l=[]
# for i in range(rows):
#     b=[]
#     for j in range(col):
#         e=int(input('enter element : '))
#         # b.append(e)
#         b.insert(j,e)
#     # l.append(b)
#     l.insert(i,b)    
# print(l)

# a='mamlamyalam'
# s1=a[0]
# print(s1)
# b=a[1:]
# print(b)
# n=b.replace(s1,'$')
# print(n)
# print(s1+n)

# a=[1,2,3,4,5]
# # l=len(a)
# # s=0
# # for i in range(l):
# #     s+=a[i]
# # print(s)

# print(sum(a))

a="malayam"
# a='recover'
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
    if count==1:        
        print(a[i])