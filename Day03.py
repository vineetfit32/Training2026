'''def welcome():
    print("Welcome to the SRMCEM")

welcome()


def read():
    print("Vineet pandey is the boss")
read()
'''
'''
def vineet():
    a=input("enter your name ")
    b=int(input("enter your roll no "))
    print(a)
    print(b)
    
vineet()

def  three():
    print("one")
    vineet()

three()
'''

'''
def greet(name, Post , batch):
    print("Hello", name, Post,batch)

greet("vineet", "IPS",2029)'''
'''

'''

#CACULATOR BY USING FUNCTION 

'''def calculator():
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number "))
    c=input("enter the operator ")
    if c == '+' :
        print(n1+n2)
    if c== '-':
        print(n1-n2)
    if c== '*':
        print(n1*n2)
        if n2!=0 and  c=='/':
         print(n1/n2)
        else :
            print("Zero Divsion Eror")
    

calculator()
    
    '''
#**kwargs
'''
def info(**data):
    print(data)

info(name="vineet",age=20)

'''
'''
def square(number):
    return number * number

result = square(5)
print(result)
'''
'''
def even_odd(n):
    if n%2==0:
        return "even"
        # print("even")
    else:
        # print("odd")
        return "odd"

print(even_odd(2))'''

'''def demo():
    x=100
    print(x)

demo()
# print(x)  ERROR'''

# c=5
# print(c)
# def count():
#     global c
#     c+=1

# count()

# print(c)

# def count(n):

#     if n>5:
#         return
#     print(n)
#     count(n+1)

# count(1)

# def count(n):
#     if n==0:
#         return
#     print(n)
#     count(n-1)

# count(10)    

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))