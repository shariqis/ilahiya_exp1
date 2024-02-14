# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows=5

# for i in range(1,rows+1):
#     # print('.........',i)
#     for j in range(i):
#         print('*', end=' ')
#     print()

# for i in range(rows,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()    


odd=1
row=5
# print(odd%2)
for i in range(1,row+1):    
    for j in range(0,i):
        print(odd , end=" ")
    odd+=2 
    print()  