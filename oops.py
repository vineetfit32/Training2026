# class  animal:
#     def sound(self):
#         print("Animal makes sound")
# class dog(animal):
#         def barks(self):
#             print("Dog barks")
# d=dog() #dog class object
# d.sound()
# d.bark()#dog class inherits animal class so it can access both sound and bark methods

# class Father:
#     def vineet(self):
#         print("vineet is the father ")
# class Son(Father):
#     def Vansh(self):
#         print("Vansh is the son")

# d=Son() #son class object
# d.vineet()


# class person:
#     name="vineet"#class variable
#     def show(self):
#         print("name", self.name)#instance method

# class student(person):
#         pass# no new functions
# s=student()#object of student class
# s.show()#accessing method of parent class



# class Teacher:
#     marks=100#class variable
#     def show(self):
#         print("marks", self.marks)#instance method  
# class student(Teacher):
#     pass  # no new functions
# d=student()#object of student class
# d.show()#accessing method of parent class   

# class father:
#     price=5000 #parrent class variable
# class son(father):
#     bike="bulllet" # Parrent Class variable is accessible in child class
# c=son()
# print(c.price)
# print(c.bike)

# class Teacher:
#     marks=90
# class student(Teacher):
#     a=int(input("Enter the marks:"))
#     if a>=90:
#         print(" Pass")
#     else:
#         print("Fail")
# c=student()


#multiple inheritance
# class father:
#     def House(self):
#         print("Give it to the Yash ")
# class mother:
#     def jwellery(self):
#         print("Give it to the Yash wife ")

# class son(father,mother):
#     pass
# Yash=son()
# Yash.House()
# # Yash.jwellery()

# class Mama:
#     def Money(self):
#         print("Give it to the Yash ")
# class Mummy(Mama):
#     def Money(self):
#         print("Give it to me")

# d= Mummy()
# d.Money()



# class Father:
#     def __init__(self):
#         print("Father class constructor")
# class Mother:
#     def __init__(self):
#         print("Mother class constructor")
# class Son(Mother,Father):
#     def __init__(self):
#         Mother.__init__(self)
#         Father.__init__(self)
# obj=Son()
# print(Son.__mro__)

# class A:
#     def show(self):
#         print("A class method")
# class B():
#     def show(self):
#         print("B class method") 

# class C(A,B):
#     pass

# print(C.__mro__)

#    MULTI LEVEL INHERITANCE


# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def eat(self):
#         print("Dog eats food")
# class Puppy(Dog):
#     def sleep(self):
#         print("Puppy sleeps")
# p=Puppy()
# p.sound() 
# p.eat()
# p.sleep()

# class Grandfather:
#     land=20
# class Father(Grandfather):
#     money=10000
# class Son(Father):
#     bike="Bullet"
# s=Son()
# print(s.land)
# print(s.money)
# print(s.bike)   


# class School:
#     def Education(self):
#         print("School provides education")
# class College(School):
#     def Degree(self):
#         print("College provides degree")
# class University(College):
#     def Research(self):
#         print("University provides research opportunities") 
# u=University()
# u.Education()
# u.Degree()
# u.Research()


# class A:
#     def __init__(self):
#         print("A class constructor")
# class B(A):
#     pass
# class C(A):
#     pass
# a=C()


# class A:
#     def __init__(self):
#         print("A class constructor")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B class constructor")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("C class constructor")    
# # a=C()



# class Animal:
#     def Eat(self):
#         print("Animal eats food")
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# d=Dog()
# d.Eat()
# c=Cat() 
# c.Eat() 


# class animal:
#     def eat(self):
#         print("Animal eats food")
# class dog(animal):
#     def sound(self):
#         print("Dog barks")
# class cat(animal):
#     def sound(self):
#         print("Cat meows")  
# c=cat()
# c.eat()
# c.sound()
# d=dog()
# d.eat()
# d.sound()   



# class A:
#     def __init__(self):
#         print("A class constructor")
# class B(A):
#     pass 
# class C(B):
#     pass
# a=C()

# b=B()

# class bank:
#     def savings(self):
#         print("Savings account")
# class Current(bank):
#     def current(self):
#         print("Current account")
# class Fixed(bank):
#     def fixed(self):
#         print("Fixed account")
# obj=Fixed()
# obj.savings()
# obj.fixed()


#       HYBRID INHERITANCE


# class A:
#     def show(self):
#         print("hello")
# class B(A):
#     pass
# class C(A):
#     pass
# class Z(B,C):
#     pass    
# obj=Z()
# obj.show() 
# print(Z.__mro__)


# USE OF SUPER KEYWORD  IN HYBRID INHERITANCE


# class A:
#     def show(self):
#         print("A class")
# class B(A):
#     def show(self):
#         super().show()
#         print("B class")
# class C(A):
#     def show(self):
#         super().show()
#         print("C class")


# obj=C()
# obj.show()



#                        DIAMOND PROBLEM QUESTION 

# class A:
#     def show(self):
#          print("A")
# class B(A):
#     def show(self):
#         super().show()
#         print("B")
# class C(A):
#     def show(self):
#         print("C")
#         super().show()

# obj=C()
# obj.show()
# print(C.__mro__)



#      polymorphism  mthod ovewriding

# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class cat(Animal):
#     def sound(self):
#         print("Cat Meows ")
# obj=Dog()
# obj.sound()
# o=cat()
# o.sound()

# class Cat:
#     def speak(self):
#         print("Cat meows")

# class Dog:
#     def speak(self):
#         print("Dog barks")

# def animal_speak(animal):
#     animal.speak()

# c = Cat()
# d = Dog()

# animal_speak(c)
# animal_speak(d)


# class shape:
#     def area(self):
#         print("Area")
# class square(shape):
#     def area(self):
#         print("area of square")
# class rectangle(shape):
#     def are(self):
#         print("area of Rectangle")
# shapes=[rectangle(),square()]
# for shape in shapes:
#     shape.area()


#    Operator polymorphisms

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __add__(self, other):
#         return self.marks + other.marks

# s1 = Student(85)
# s2 = Student(90)

# print(s1 + s2)


#                   DUCK TYPING  

# class student():
#     def work(self):
#         print("student is studying")
# class teacher:
#     def work(self):
#         print("teaching ")
# def perform(person):
#     person.work()
# s=student()
# t=teacher()
# perform(s)
# perform(t)


#public 
# class student:
#     def __init__(self):
#         self.name="Ram"
#     def show(self):
#         print(self.name)# public variable acces inside the class 
# obj=student()
# obj.show()#public method 
# print(obj.name) #Public variable access outside the class 

#protected

# class student:
#     def __init__(self):
#         self._name="Vineet IS the BOSS"  # Protected Variable 
#     def show(self):
#         print(self._name)
# obj=student()
# obj.show()
# print(obj._name)  # GIVES ACCESS BUT IT IS RECOMENDED



#  Private---------------->  By Double Under Score 



# class student:
#     def __init__(self):
#         self.__name="vineet"
#     def show(self):
#         print(self.__name)
# o=student()
# o.show()
# print(o.__name)




#************************************GETTER AND STTER CONCEPT IN ENCAPSULATION**********************************************




# class  student:
#     def __init__(self):
#         self.__name="Vineet"

#     def get_mark(self):    #GETTER
#         return self.__name
# obj=student()
# print(obj.get_mark())  # ACCESS THE VARIABLE THE GETTER METHOD 

# class Student:
#     def __init__(self):
#         self.__marks = 0      # Private variable

#     # Setter method
#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Marks should be between 0 and 100.")

#     # Getter method
#     def get_marks(self):
#         return self.__marks


# # Creating an object
# s1 = Student()

# # Setting marks
# s1.set_marks(85)

# # Getting marks
# print("Student Marks:", s1.get_marks())



#*******************  NAME MANGLING METHOD ************************


# class  student():
#     def __init__(self):
#         self.__name="yash"
# obj=student()
# print(obj._student__name)



#****************  ABSTRACTION *************************
# from abc import ABC , abstractmethod 
# ABC  == Abstract based class 
#abc == MODULE 

# class animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class dog(animal):
#     def sound(self):
#         print("dog barks ")
# obj=dog()
# obj.sound()




#*******************  MULTIPLE  ABSTRACTION ******************

# class vehicle:
#     @abstractmethod
#     def start(self):
#         pass
#     def stop(self):
#         pass
# class bike(vehicle):
#     def start(self):
#         print("Bike start")

#     def stop(self):
#         print("Bike stop")
# obj=bike()
# obj.start()
# obj.stop()




