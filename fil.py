# ##file open

# # file = open('anu.txt','r') 
# # # # file = open(r"C:\Users\quest\Desktop\Shari\MyWorks\fileOpp.txt.txt",'r')  # specifying full path
# # # # file = open(r'D:\new.txt.txt','r') 
# # # # This will print every line one by one in the file 
# # print(file)
# # for n in file: 
# #     print(n) 

# # # Python code to illustrate read() mode 
 
# # print (file.read(6)) 
# # c=file.read()
# # print(c)
# # print(len(c))
# # # Python code to illustrate read() mode character wise  
# # #way to read a file is to call a certain number 
# # of characters


# # print (file.read(4))



# # # # # Python code to create a file 
# # f=open(r'D:\batch_ilahiya\shani.txt','w')
# # # f=open(r'D:\d1\alwin.txt.txt','w')
# # # # # f = open(r'D:\newbatch\file1.txt','w') 

# # f.write("This is the write command 1nd") 
# # f.write('\n')
# # f.write("This is the write command dskjfhdskjhfkdjsf") 

# # f.write('welcome')
# # f.close() 
# # f.write('welcome')

# # # # # # Python code to illustrate append() mode 
# # file = open('anu.txt','a') 
# # file.write("This will add this line 67698789") 
# # file.close()


# # # # # Python code to illustrate with() alongwith write() 
# # with open("v.txt", "r") as f:  # f= open("v.txt", "w")
# #     print(f.read())
#     # f.write("Hello World!!!")  

# # # # # Python code to illustrate split() function 
# with open("anu.txt", "r") as file: 
#     # data = file.read() 
#     data = file.readlines() 
#     print(data)
#     print('----------------------')
#     # print(data[1:4])
# #     print('----------------------')
#     for line in data: 
#         word = line.split('\n') 
#         print (word) 


a="malayalam"
print(a[4:19])
# b=a.replace('m','#',6)
# print(b)