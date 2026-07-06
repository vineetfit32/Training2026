
# try:
#   age=int(input("enter the age "))
#   print(age)
# except:
#     print("enter the valid age :")


# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Division by zero not allowed")



# Finally 


# try:
#     print(10/0)
# except:
#     print("not allowed ")
# finally:
#     print("executed")


# try:
#     print(10//2)
# except:
#     print("error ")
# else:
#     print('not error')
# finally:
#     print("executed")



# To raise an error 


# age=int(input("enter the age "))
# if age<18:
#     raise ValueError("Age must be 18")
# print("eligible to vote ")


#as

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e) 



#make a calculator by using Try AND Except Block


a=float(input("Enter the first number"))
b=float(input("Enter the sdcond number "))
c=input("Choose the operator such as + - * / \n : ")
try:
    if c=='+':
        print(a+b)
    if c=='-':
        print(a-b)
    if c=='*':
        print(a*b)
    if c=='/':
        print(a/b)
except ZeroDivisionError as e :
    print(e)