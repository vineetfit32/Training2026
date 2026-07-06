#list
list=[]
print(type(list))
l1=[10,2.0,"vineet","a+1b"]
print(l1)

l2=[1,2,[3,4,5],5]
print(l2)

l3=[1,2,3]
print(l3[0])
print(l3[::])
print(l3[0:])

l3[-1]=4
print(l3)
L=l3+l2
print(L)
print(l2*3)
print("***********************************************************************************************")



#append
l1.append(42)
print(l1)

#remove

l1=[1,2,3,4]

l1.remove(1)
print(l1)
l1.pop()
print(l1)



