# a={2,5,44,11,3,88,2,44}
# print(a)
# # print(type(a))
# # a=set()
# # # a='haiia'
# # print(a)
# # print(type(a))

# a={1:100,2:500,3:300,4:500}
# print(a)
# n=a.items()
# # print(n)
# # c=set(a)
# # print(c)

# m=set(n)
# # print(m)
# a={11,33}
# # print(a)
# # a.add((45,88))
# # print(a)
# a.add('hii')
# print(a)
# # a.add([55,88,55])
# # print(a)

# a=('hii',)
# print(type(a))

# a={3,8}
# print(a)
# print(type(a))


# a={2,5,44,11,3,88}
# print(a)
# # a.remove(56)
# a.discard(56)
# print(a)


# a={1,2,3,4,5}
# b={4,5,6,7,8}

# # # print(a|b)
# # # print(a&b)
# # # print(b-a)
# # print(a^b)


# a="welcome"  # 3

# b=set(a)


# d=list(a)
# print(d)

# for i in b:
#     d.remove(i)
    
# print(d)    
    

# # a={1,2,3}
# # for i in a:
# #     print(i)

# n={1,2,3,4,5,6,7,8,9,10}
# e={2,4,6,8,10}
# o={1,3,5,7,9}
# # print(e.isdisjoint(o))
# # print(o.issuperset(n))
# print(o.issubset(n))


# {}, set(), [], ()

# a={5,6,7,8}
# b={7,8,10,11}
# a^b

# s={5,6}
# print(s*3)

# a=[5,6,7,8]
# b=[7,5,6,8]
# print(a==b)

# a={3,4,{7,5}}
# print(a)

# a=('ch',)

# n=2

# for i in range(int(n)):
#     a=(a,)    # ((ch,),)    (((ch,),) ,)
#     print(a)
    
# a,b=1,2,3    

# a=(1,2)
# b=(3,4)
# print(id(b))
# b=a+b
# print(b)  # (4,6), (1,2,3,4)
# print(id(b))
# a=[1,4]
# print(id(a))
# a.append(8)
# print(id(a))

a=(4,8,6)
# print(a[1:])

print(sorted(a))
print(dir(a))