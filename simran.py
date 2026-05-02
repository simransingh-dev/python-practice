# name = input("Enter your name: ")
# print("Hello", name + ", welcome to Python!")



# # 2. Calculator
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Sum:", a + b)
# print("Difference:", a - b)
# print("Product:", a * b)
# print("Division:", a / b)



# # 3. Even or Odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# # 4. Largest of Two Numbers
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# if x > y:
#     print(x, "is greater")
# else:
#     print(y, "is greater")



# # 5. Swap Two Numbers (without third variable)
# p = int(input("Enter first number: "))
# q = int(input("Enter second number: "))

# p, q = q, p

# print("After swapping:")
# print("p =", p)
# print("q =", q)


# # 6. Square and Cube
# n = int(input("Enter a number: "))
# print("Square:", n ** 2)
# print("Cube:", n ** 3)


# # 7. Simple Interest
# P = float(input("Enter principal: "))
# R = float(input("Enter rate: "))
# T = float(input("Enter time: "))

# SI = (P * R * T) / 100
# print("Simple Interest:", SI)



# # 8. Temperature Converter
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:",
#  fahrenheit)



# conditional statements
# age=23

# if (age >=18):
#     print("can vote and apply for licensce")
# #     print("can drive too")

# light="red"

# if (light =="pink"):
#     print("stop")
# elif( light =="green"):
#     print("go")
# elif( light =="yellow") :
#     print("look")
# else:
#     print("light is broken")

# age=14

# if (age >=18):
#     print("can vote and be finanviallyu independent") 
# else:
#     print("you are still a kid according to society..but who cares ")


# grade students according to their marks 

# marks=88
# marks=int(input("enter student marks:"))

# if(marks >=90):
#     grade="A"
# elif (marks >= 80 and marks < 90) :
#     grade="B"
# elif (marks >= 70 and marks < 80) :
#     grade="C"
# elif (marks >= 60 and marks < 70) :
#     grade="D"
# else:
#     print("you are a losser according to brainwashed people")

# nesting is writting one statement into another statement 

# age=98

# if (age >=18) :
#     if (age >=80):
#         print("cannot drive ")
#     else:
#         print("can drive ")
# else:
#     print("cannot drive ")

#  check if a number is odd or even 

# num= int(input("enter a number :"))

# if num % 2 ==0:
#     print("even number")
# else:
#     print("odd number ")

# find greatest of 3 numbers 

# a=int(input("enter first number :"))
# b=int(input("enter second  number :"))
# c=int(input("enter third number :"))

# if a >= b and a >= c :
#     print("greatest is :" , a)
# elif b >= a and b >=c :
#     print("greatest is :" , b)
# else:
#     print("greatest is :" , c)

#  check if a number is multiple of 7 

# num=int(input("Enter a number : "))

# if num % 7 ==0:
#     print("it is a multiple of 7")
# else:
#     print("not multiple of 7")

# list
# marks1=43
# marks2=43
# marks3=43
# marks4=43
# marks5=43

# marks=[43,43,43,43,43]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(len(marks))

# student=["shivani",98.3,22,"Delhi"]
# print(student)
# print(student[3])

# list are mutable in python
# sublist is a small part of a list
# LIST SLICING
# marks=[10,90,70,80]
# print(marks)
# print(marks[1:3])

# list methods 

# list = ["a","b","c","d"]

# list.append(4)
# # print(list.sort())
# print(list)
# print(list.sort(reverse=True))

# list=[2,1,3,4]
# list.remove(1)
# print(list)

# tuples in python - it is a built -in data type that lets us create immutable sequences of values

# we use parenthesis instead of square bracket

# tup=(2,3,4,1)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(type(tup))

# tup=("hello",)
# print(tup)
# print(type(tup))

# slicing in tupple works the same way as in strings and lists
# tup=(1,2,3,4)
# print(tup[1:3])
# print(type(tup))

# tuple methods 
# tup=(1,2,3,4,5)
# print(tup.index(2))
# print(tup.count(2))

# ask user for 3 favourite movies and store in a list

# movies=[]

# for i in range(3):
#     movie=input(f"enter your {i+1} favourite movie:")
#     movies.append(movie)

# print("your favourite movies are :",movies)

# check if a list is pallindrome

# list=[1,2,3,2,1]

# copy_list=list.copy()
# copy_list.reverse()

# if list ==copy_list:
#     print("palliondrome")
# else:
#     print("not a pallindrome")

# count

# grades=("c","d","A","B")

# list=list(grades)
# list.sort()
# print(list)


# grades=("c","A","B","D","c")
# list=list(grades)
# list.sort()
# print(list)

# dictionary in python
# dictionaries are used to store data values in key:value pair
# they are unordered, mutable(changebale) and do not allow duplicate keys

# dict={
#     "name" : "simran",
#     "cgpa": 9.9,
#     "subject":["maths","science","sst"]
# }


# print(dict)

# student={
#     "name":"Shivani",
#     "class":"10nth",
#     "subjects": ["hindi","english","Maths","Hindi"],
#     "age":15,
#     "is_adult": False
# }

# print(student)


# null_dict={}

# print(null_dict) we can null dictionary like this too

# NESTED DICTIONARY
# student={
#     "name":"Saanvi",
#     "cities": {
#         "delhi",
#         "mumbai",
#         "patna"
#     }
# }

# print(student)
# set is a collection of unordered item , each element in the set must be unique and immutable

# collection={1,2,3,4,4}

# print(collection)
# print(type(collection))

# collection= set()
# print(type(collection))

# there are different set methods like
# set.add() - it adds an element
# set.remove() - it removes an element
# ṣet.clear() - it empties the set
# set.pop() - removes random number
# set.union(set2) - combines both set values and returns new
# set.intersection(set2) - combines common values and returns new

# collection={"hello","simran"}
# print(collection.pop())

# store word meaning in a dictionary

# words={
#     "table" : ["a piece of furniture", "lists of facts and figures"],
#     "cat": "a small animal"
# }
# print(words)

# no of classroom needed
# subject=["python","Java","c++","Javascript","Java"]
# unique_subjects= set(subject)

# print(len(unique_subjects))

# store 9 and 9.0 separately
# s={9,9.0,"9"}
# print(s)

# loops in python

# loops are used to repeat instructions

# there are two types of loops in python
# while loop and for loop

# for i in range( 1,11):
#     print(i)

# i=1
# while i <=10:
#     print(i)
#     i+=1

# print i in range(1,21):
# for i in range(1,21):
#     if i %2== 0:
#         print(i)

# print sum of numbers from 1 to n

# n=int(input("Enter a number :"))
# total=0

# for i in range(1,n+1):
#     total += i

#     print("sum:",total)

# print multiplication table of a number

# n=int(input("Enter a number:"))

# for i in range(1,11):
#     print(n, "x" , i , "=" , n* i)

# i=1

# while i <=10:
#     print(i)
#     i+=1

# i=1

# while i <=20:
#     if i % 20:
#         if i % 2==0:
#             print(i)
#             i +=1


# find sum of numbers from 1 to 100

# i=1

# while i <=20:
#     if i %2==0:
#         print(i)
#         i +=1

# functions in pythons- block of statements that perform a specific task
# def func_name(param1,param2..);
#   some work
# return value

# func_name(arg1,arg2...) - function call


# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum

# calc_sum(2,2)
# calc_sum(2,23)
# calc_sum(12,12)

# def calc_sum(a,b) : function definaiton
#     return a+b

# # sum=calc_sum(1,2)  function call
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()

# average of 3 numbers

# def calc_average(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg

# calc_average(1,2,3)

# there are different types of functions in python 
# 1.built in  2. User-defined function

# print("Simran")
# print("A Software developer")


# length len(), type(), range(), print()   these are all built in function


# def calc_prod(a=7,b=8):
#     print(a*b)
#     return a*b

# calc_prod()


# print length of a list 
# def print_length(lst):
#     print("length of list:", len(lst))

# # OUTSIDE the function
# my_list = [1, 2, 34, 4]
# print_length(my_list)

# print elements of a list in a single line 

# def print_elements(lst):
#     for i in lst:
#         print(i,end="")

# print_elements([1,2,34,4,5])


# find factorial of n 

# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact *=i
#     print(fact)
# factorial(5)

# Convert usd to inr

# def usd_to_inr(usd):
#     rate=90
#     inr=usd*rate
#     print(inr)

# usd_to_inr(5)

# file input and output in python

# all the variables are created in ram but the probem is ram is volatile

# python can be used to perform operations on a file . ( read and write data )

# types of all files

# 1. text files - .txt, .docx, .log etc
# 2. binary files  - .mp4, .mov, .png, .jpeg

# at the end all of them are stored as 0 and 1 

# OPEN,READ AND CLOSE FILE
# we have to open a file before reading or writting


# oops in python
# to map with real world secenarios, we started using objects in code .
# this is called object oriented programming.
# because of function redundency decrese and reusebility increased 
# everything around us is an object . firstly we make a class then we create an object .

# CLASS IS A BLUEPRINT FOR CREATING AN OBJECT
# creating class

# class Student:
#     name="Simran Singh"
   

# # creating an object

# s2= Student 
# print(s2.name)



# class Car:
#     color="blue"
#     brand="mercedes"

# car1=Car()
# print(car1.color)
# print(car1.brand)

# CONSTRUCTOR - INIT FUNCTION 
# all clases have a function called _init_(),
# which is always executed when the class is being initiated
# 1. creating class

# class Student:
#     def __init__(self, fullname):
#         self.name=fullname
       

# creating object

# s1=Student("Saanvi")
# print(s1.name)

# s2=Student("simiii")
# print(s2.name)
# The self parameter is a reference to the current
# instance of the class, and is used to acess
# variables that belongs to the class.

# all the data that is stored in the class are called attributes.

# class and instance attribute
# class.attribute
# object.attribute

# class Car:
#     def __init__(self, userbrand, usermodel):
#         self.brand = userbrand
#         self.model = usermodel

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)

# class Student:
#       def set_name(self,name):
#           self.name=name
          
#       def get_name(self):
#           return self.name

# Student1 =Student()
# Student1.set_name("Simran")
# print(Student1.name)
# print(Student1.get_name())

# Student2 =Student()
# Student2.set_name("Saanvi")
# print(Student2.name)
# print(Student2.get_name())

# Student3 =Student()
# Student3.set_name("Shivani")
# print(Student3.name)
# print(Student3.get_name())

# Create a class person with name,age and print them

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# p1=Person("Shivanii",20)


# print("Name :" , p1.name)
# print("Age :" , p1.age)

# add a method to display details
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def show_details(self):
#         print(f"my name is {self.name }and i am {self.age} years old")
        
# p1=Person("Shivanii",20)

# p1.show_details()

# class Book :
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

# b1=Book("Python Basics", "Simran")

# print("Title:" , b1.title)
# print("Author:" , b1.author)


# class Book :
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

#     def show(self):
#          print(f"{self.title} by {self.author}")
         
         
# b1 = Book("Python basics", "Simran")
# b1.show()

# class Laptop:
#     def __init__(self,brand,price):
#         self.brand= brand
#         self.price= price
        
# l1 = Laptop("HP", 25000)

# print(l1.brand)
# print(l1.price)

# class Laptop:
#     def __init__(self,brand,price):
#         self.brand= brand
#         self.price= price
        
#     def details(self):
#         print(f"Laptop :{self.brand} , Price : {self.price}")
        
        
# l1=Laptop("HP",25000)
# l1.details()

# class Movie :
#     def __init__(self, name,rating):
#         self.name=name
#         self.rating=rating
# m1 = Movie("Inception", 9)

# print(m1.name)
# print(m1.ratingclass Movie :


# class Movie :
#     def __init__(self, name,rating):
#         self.name=name
#         self.rating=rating
        
#     def review(self):
#         print(f"{self.name} has rating {self.rating}")
        
# m1=Movie("Inception", 9)
# m1.review()


# Store name and subject

class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
        
t1 = Teacher("Simran", "python")

print(t1.name)
print(t1.subject)
