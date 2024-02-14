

a="get"
b='set'
# for i in a:
#     for j in b:
#         print(i,j)

# m=[i+j for i in a for j in b]
# print(m)


# a=[]
# for i in range(5):
#     a.append(i)
# print(a)

# a=[i for i in range(5)]
# print(a)

n=[2,43,67,52,77,12]
# a=[]
# for i in n:
#    if i%2==0:
#        a.append(i) 
# print(a)


# a=[True for i in n if i%2==0]
# print(a)

# n=[2,43,67,52,77,12]
# print(n)
# a=['e'if i%2==0 else 'o' for i in n ]
# print(a)


# a=[i for i in range(1,100) if '6' in str(i) if 66!=i]
# print(a)

# a="my name is shari"
# b=a.split()
# print(b)
# c={}
# for i in b:
#     c[i]=len(i)
# print(c)    


# v={i:len(i) for i in a.split()}
# print(v)

# Use a nested list comprehension to 
# find all of the numbers from 1–1000 that are
# divisible by any single digit besides 1 (2–9)

# q7_answer = [num for num in range(1,50) if True in [True for divisor in range(2,10) if num % divisor == 0]]


# print(q7_answer)


num=22
v=[0 for divisor in range(2,10) if num % divisor == 0]
print('...........')
print(v)



# [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15,
#  16, 18, 20, 
#  21, 22, 24, 25, 26, 27, 28, 30, 32, 33,
#  34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49]