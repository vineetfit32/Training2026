
# try:
#   age=int(input("enter the age "))
#   print(age)
# except:
#     print("enter the valid age :")


try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero not allowed")