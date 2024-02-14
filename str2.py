# str = "welcome"
# print(str)

# print(str[0:])
# print(str[:3])
# print(str[:5])
# print(str[0:2])
# print(str[1:5])
# print(str[:-5:-2])
# print(str[:-5])
# print(str[-5:-1])








## String Padding Functions
# #
# var='Hi'
# print(var)
# # print (var.rjust(5))
# # print (var.rjust(10,'*'))
# # print (var.ljust(10))
# # print (var.ljust(10,'-'))
# # print (var.center(6,'*'))
# print (var.zfill(10))



# var='*****This is *** a good example*****'
# print(var)
# print(var.strip('*'))
# # print (var.lstrip('*'))
# # var='*****This is a good example*****'
# # print (var.rstrip('*'))



# # Functions To Find A String In Python.
# Var = 'welcome'
# # print( Var.find('o',2,4))
# # print( Var.find('hello'))
# # print( Var.index('u'))
# # print( Var.index('hello'))
# print( Var.rfind('e'))



# var='This is a good example'
# str='is'
# print (var.count(str,7))
# # # print (var.find(str))
# # # print (var.rfind(str))
# print (var.replace('is','was',6))


# a="restart"
# v="aeiou"  # rstrt
# b=''
# for i in a:
#     if i not in v:
#         b+=i
# print(b)        


# a="dfdf ss ss saswew rer"
# # print(a.count(' '))
# c=0
# for i in a:
#     if i==" ":
#         c+=1

# print(c)        



# a="hai hello welcome to qis"
# # a='welcome'
# c=a.split(' ')

# for i in c:
#     if len(i)<5:
#         print(i)



for i in range(1,101):
    if i//10==6 or i%10==6 :
        if i//10==6 and i%10==6:
            continue
        print(i)