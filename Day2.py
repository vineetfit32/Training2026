'''age=int(input("enter the Age "))
if age>=18:
    print("you are eligible to vote ")
else:
    print("You are minor")

num=(int(input("enter any number ")))
if num%2==0:
    print("it's a Even number ")
else:
    print ("odd number")
'''
'''m=int(input("Enter The marks of maths "))
p=int(input("enter the marks of Physics "))
c=int(input("enter the marks of Chemistry "))

average=(p+c+m)/3
if average >=90:
    print("Grade=A")
elif average>=80:
    print("Grade=B")
elif average>=75:
    print("Garde=C")
print("Your Average MArks Are",average)'''


#loan Approved 

'''age=int(input("enter the age "))
salary=int(input("enter the salary "))

if age >=25 and salary>=50000:
    print("The LOAN Can Be Approved ")
else:
    print("LOAN Can't Be Approved ")'''

#Weekend

'''Day=input("enter the Day")
if Day==SATURDAY or Day==SUNDAY or Day==Sunday or Day==Saturday or Day==sunday or Day==satuday:
    print("It's a weekend ")
else:
    print("not a weekend ")'''

#largest between three
'''
a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))

if a>b and a>c:
    print("a is the greatest ")
elif b>c and b>a:
    print("b is the greatest ") 
elif c>a and c>b:
    print("c is the greatest ")
else:
    print("all are equal")'''


#Program to check whether a year is a leap year
'''
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a Leap Year")
elif year % 100 == 0:
    print(f"{year} is NOT a Leap Year")
elif year % 4 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")



# Program to check whether a character is a vowel

char = input("Enter a character: ").lower()

if char in "aeiou":
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")
'''

'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    print("Result =", num1 + num2)

elif choice == "2":
    print("Result =", num1 - num2)

elif choice == "3":
    print("Result =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid choice Please select 1, 2, 3, or 4.")'''

#sum of first n natural number

# Sum of first n natural numbers
'''
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum", sum )
'''

#Factorial of number 

n=int(input("enter the number "))
factorial=1
if n==0 or n==1:
    print("the Factorial is 1")
else:
    for i in range(1,n+1):
        factorial*=i
print("the factorial is ",factorial)

# Program to check if a number is a palindrome

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")