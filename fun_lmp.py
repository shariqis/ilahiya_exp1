#  lambda arguments: expression

# x=lambda a:   v= 4*a
# print(x(2))

# x1=lambda a:10+a
# print(x1(9))

# x2=lambda a,b,c: print(c)

# # x2(3,2,1)
# print(x2(3,2,1))



# def add(a):
#     c=a*5
#     return c
# v=add(5)
# print(v)

# def myfun(n):
#     return lambda a:a*n  # lambda a:a*2


# d=myfun(2)
# print(d(5))

# t=myfun(3)
# print(t(5))



# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
# final_list = list(filter(lambda x: (x%2 != 0) , li)) 
# print(final_list) 


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 



from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x-y), li) 
print (sum)

