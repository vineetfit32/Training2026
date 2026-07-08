# # 

# file=open("Vineet!.txt",'a+')
# data=file.read()
# file.close()
# # print(data)


# file=open("vineet.txt",'r+')
# print(file.read(5))


# file=open("vineet.txt",'r+')
# print(file.seek(5))

# file=open("vineet.txt","r+")
# print(file.tell())
# file.read(4)
# print(file.tell())
# file.close()


# with open("vineet.txt","r+") as file :
#     data=file.read()
#     print(data)

# file = open("vineet.txt", "a")

# print(file.tell())   # Position before writing

# file.write(" Python")

# print(file.tell())   # Position after writing

# file.close()




# def get_pair(a,b=5):
#     return a+b
# print(get_pair(3))


#lambda a,b:a+b
#lambda = parameters + expression 

# s=lambda X:X*X
# print(s(5))

# sub=lambda y,z:y-z
# print(sub(5,4))

# m=lambda m,n:m*n
# print(m(55,1))

# d=lambda num,din:num/din
# print(d(15,5))

# c=lambda x:x**3
# print(c(3))

# z=lambda a: a %2==0
# print(z(50))



#map(fuction , iterable)
# num=[1,2,3,4,5]
# r=map(lambda x:x*2,num)
# print(list(r))

# num=[25,25,26,27]
# r=map(lambda x:x+20,num)
# print(tuple(r))

# r=['ram','shyam']
# res=map(str.upper,r)
# print(tuple(res))


# FILTER

# name=['Aman','Ashish','Rahul','Vineet']
# res= filter(lambda x:x.startswith('A'),name)
# print(list(res))


#  REDUCE

# from functools import reduce
# num=[10,20,30]
# d=reduce(lambda a,b : a+b , num )
# print(d)


