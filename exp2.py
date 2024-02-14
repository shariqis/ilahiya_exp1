class Lessthan10(Exception):
    def __str__(self):
        return "Enter NUmber greater than 10"

        
try:
    a=5/0
    
    a=int(input("Enter the number greater than 10: "))
    if a<10:
        raise Lessthan10()
    # b=int(input("Enter the number: "))

    

except ZeroDivisionError as d :
    print(d)
    print(ZeroDivisionError)
    print("Enter a non zero value")
# except ValueError as c:
#     print(c)
#     print("Enter a number")
except Lessthan10 as e:
    print(e)
    print('mmmmmmmmmmmmmmm')
# else:
#     print("HELOOWORLD")
# finally:
#     print("rfgergret")



# x = "hello1"

# # if condition returns True, then nothing happens:
# # assert x == "hello"

# #if condition returns False, AssertionError is raised:
# assert x == "goodbye",'mmmmmmmmmmmmmmmmmmmmmmm'



