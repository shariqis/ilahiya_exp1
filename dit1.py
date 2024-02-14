# # a={'name':'shari','place':'eklm'}
# # print(a)
# # print(type(a))
# # print(a['name'])
# # a['name']="shari S"
# # print(a)
# # a['phn']=3647324
# # print(a)
# # print(len(a))
# # for i in a:
# #     print(i , a[i])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict)


# # #Accessing Items

# # # x = thisdict["model1"]
# # # print(x)
# # x = thisdict.get("model",'error')
# # print(x)



# # ## to get values
# # for x in thisdict.values():
# #   print(x)

# ## dictionary keyvalue paird
# # for x, y in thisdict.items():
# #   print(x, y)


# # if 'Ford' in thisdict:
# #     print('yes')
# # else:
# #     print('No')    


# # # ## pop with key
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # print(thisdict)
# # c=thisdict.pop("model")
# # print(thisdict)
# # print(c)


# # ## popitem() - last inserted item
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # n=thisdict.popitem()
# # print(thisdict)
# # print(n)
# ##delete
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # del thisdict["2rmodel1"]
# # print(thisdict)


# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict.clear()
# # print(thisdict)



# # while True:
  
# #   choice=int(input(''' enter choice 
# # 1 -> Add
# # # 2 -> sub
# # # 3 -> mul
# # # 4 -> div
# # # 5 -> exit  :  '''))
  
# # #   if choice==1:
# # #     print('add')  
# # #   elif choice==2:
# # #     print('sub') 
# # #   elif choice==3:
# # #     print('mul')
# # #   elif choice==4:
# # #     print('div')
# # #   elif choice==5:
# # #     print('exit')
# # #     break
# # #   else:
# # #     print('invalid')  
     




# # prices = {'Apple': 1.99, 'Banana': 0.99,
# #           'Orange': 1.49, 'Cantaloupe': 3.99,
# #           'Grapes': 0.39}
# # print(prices)
# # # print(sorted(prices))
# # # print(sorted(prices.keys()))

# # # print(sorted(prices.values()))
# # # print(sorted(prices.items()))
# # print (sorted(prices.values(), reverse=True))

# pb={}
# while True:
#   choice= int(input('''enter choice 
#     1 -> Add
#     2 -> View
#     3 -> Update
#     4 -> Delete
#     5 -> Exit :  '''))
  
#   if choice==1:
#     sub={}
#     name=input('enter name : ')
#     email=input('enter email : ')
#     phone=int(input('enter phone : '))
#     sub['name']=name
#     sub['email']=email
#     sub['phone']=phone
#     pb[name]=sub
#   elif choice==2:
#     fullserch=int(input('enter choice 1 -> full view 2 -> serach'))
#     if fullserch==1:
#       print(pb)
#     else:
#       name=input('enter name to search -> : ')
#       if name in pb: 
#         print(pb[name])
#       else:
#         print('invalid name')  
#   elif choice==3:
#     name=input('enter name to update -> : ') 
#     print(pb)   
#     if name in pb:
#       update_choice=int( input('''
#       1-> update name
#       2-> update num
#       3-> update email
#       :  '''))
#       if update_choice==1:
#         new_name=input('enter new name : ')
#         pb[name]['name']=new_name
#         n=pb.pop(name)
#         print('............',n)
#         pb[new_name]=n
#         print(pb)
#       elif update_choice==2:
#         new_ph=int(input('enter new num : '))
#         pb[name]['phone']=new_ph
#         print(pb)
#     else:
#       print('invalid')    