#All Functions With Pattern printing 

# factorial of a number 

# def factorial(n):
#     fact =1
#     for i in range (1,n+1):
#         fact*=i

#     return fact 
# print("factorial of number is :", factorial(5))



# To check the prime number 

# def prime(n):
#     if n<=1:
#         return "not prime"
#     for i in range (2,n):
#         if n%i==0:
#             return "not prime "
#     return "prime " 

# print (prime(27)) 
# print(prime(19))  


# Reverse the number 

# def reverse_of_number (n):
#     rev=0
#     while n>0:
#         digit = n%10
#         rev=rev*10 + digit 
#         n= n//10
#     return rev 

# print(reverse_of_number(1211))



# Sum of digits 

# def sum_f_digits(n):
#     total =0

#     while n>0:
#         digit = n%10
#         total += digit 
#         n = n//10

#     return total 
# print( sum_f_digits (456))

#reverse of text


# def reverse_string(text):
#     return text[::-1]

# print(reverse_string("Python"))



# Count of Vowel 

# def count__vowels(text):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for ch in text:
#         if ch in vowels:
#             count+=1
#     return count 
# print (count__vowels("vineet"))


# Fibonacci series 

# def fibonacci(n):
#     a=0
#     b=1

#     for i in range(n):
#         print(a,end =" ")
#         a, b = b, a+b
# fibonacci(10)


# Pallindrone 

# def pelindrome(text):
#     if text == text [::-1]:
#         return "Palindrome"
#     else:
#         return "Not A Palindrome"
    
# print(pelindrome("madam"))
# print(pelindrome("vinnet"))
            



# PATTERN PRINTING QUESTIONS 

# *
# **
# ***
# ****
# *****
# ******

# for i in range (1,7): 
#     print("*"*i)




# 2 

# *****
# ****
# ***
# **
# *

# rows = 5

# for i in range(rows, 0, -1):
#     print("*" * i)





