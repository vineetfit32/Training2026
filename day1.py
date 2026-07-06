print("hello world")
a=True 
b=False 
print(type(a))
print(type(a&b))
a='Vineet Pandey'
print(type(a))
print(a[:6] )
print(a[7:])
print(a[::-1])

#Type Casting by using int function 

print(int(222.222))
print(int(3+3j)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

print(float(3+6j)) #Type error 

print(float("vvv"))#Type error '''


print(float(False)) #0.0
print(float(True)) #1.0
print(complex(False,True))
print(complex(True,True))

print(complex(10.5,2))

print(bool(complex(0.0)))
print(bool(complex(0.1)))
print(bool(complex(55)))

print(bool(5))
print(bool(complex(0)))





