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

# class Teacher:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
        
# t1 = Teacher("Simran", "python")

# print(t1.name)
# print(t1.subject)


# class Teacher:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
        
#     def introduce(self):
#         print(f"My name is {self.name}, I teach {self.subject}")
        
# t1=Teacher("simran","Javascript.")
# t1.introduce()


# class Mobile:
#     def __init__(self , brand,price):
#         self.brand=brand
#         self.price=price
        
#     def show(self):
#         print(f"{self.brand} costs {self.price}")
        
# m1=Mobile("Samsung",20000)
# m1.show()
        
        
# class City:
#     def __init__(self, name , state):
#         self.name=name
#         self.state=state
        
#     def show(self) :
#         print(f"{self.name} is in {self.state}")
              
              
# c1=City("Patna","Bihar")
# c1.show()



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def show(self):
#         print(f"{self.name} scored {self.marks}")
        
# s1=Student("Simran", 79)
# s1.show()


# class Car:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed
    
#     def drive(self):
#         print(f"{self.brand} is running at {self.speed} km/h")
        
# c1=Car("BMW",120)
# c1.drive()


# Bank account

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
    
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"{amount}deposited")
        
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             print(f"{amount}withdrawn")
            
#     def show_balance(self):
#         print(f"balance:{self.balance}")
        
# acc=BankAccount("Simran",9700)
# acc.deposit(500)
# acc.withdraw(200)
# acc.show_balance()

# class Mobile:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
        
#     def discount(self,percent):
#         self.price-=(self.price* percent /100)
        
#     def show(self):
#         print(f"{self.brand} costs {self.price}")
        
# m1 = Mobile("Samasung",33000)
# m1.discount(10)
# m1.show()


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Area:", self.length * self.width)

#     def perimeter(self):
#         print("Perimeter:", 2 * (self.length + self.width))


# r1 = Rectangle(10, 5)
# r1.area()
# r1.perimeter()

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def display(self):
#         print(f"Name : {self.name} , Marks : {self.marks}")
        
# s1=Student("SImran Singh" , 90)
# s1.display()

# inheritance

# class Animal:
#     def speak(self):
#         print("Animal Speaks")
        
# class Dog(Animal):
#     def bark(self):
#         print("dog barks")
        
        
# d=Dog()
# d.speak()
# d.bark()
    
    
    # polymorphism
    
    
# class Dog:
#     def sound(self):
#         print("Bark")
        
# class Cat:
#     def sound(self):
#         print("Meow")
        
# for animal in [Dog(),Cat()]:
#     animal.sound()
    
    # student grade system 
    # store syudent name and marks list, method to calculate average and method to display result
    
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def average(self):
#         return sum (self.marks) / len(self.marks)
    
#     def result(self):
#         avg=self.average()
#         if avg >=40:
#             print("Pass")
#         else:
#             print("Fail")
            
            
# s1=Student("Simran",[50,20,80])
# s1.result()

# s2=Student("Riya",[20,10,20])
# s2.result()

# s2=Student("Shivani",[20,100,20])
# s2.result()

# s2=Student("Saanvi",[20,60,20])
# s2.result()


# s2=Student("Sneha",[10,10,20])
# s2.result()

# s2=Student("Priyanka",[80,100,20])
# s2.result()

# variable is a reusable container for a value (strinh, integer,float,boolean)
# the variable behaves as if it was the value it contains.

# full_name ="Scarlett"
# age=23
# gpa=70
# girl=True
# print(full_name)
# print(age)
# print(gpa)
# print(girl)
# if girl:
#     print("you are student")
# else:
#     print("You are not a student")

# friends=3
# friends +=9
# print(friends)

# friends =9
# friends-=1
# print(friends)

# friends=8
# friends*=2
# print(friends)

# friends=7
# friends%=2
# print(friends)

# friends=6
# friends**=9
# print(friends)

# friends=10
# remaining_friends = friends %2
# print(remaining_friends)

# Type Casting

# name="scarlett"
# age=23
# gpa=6.0
# is_student=True

# gpa =int(gpa)

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))

# name=input('Enter your name:')
# age=input("Enter your age :")
# print(name)

# if statements
# age=int(input("Enter your age:"))

# if age >= 18:
#     print("You are an adult")
# else :
#     print("You are a child")

# logical operators
# or- atleast one condition must be true
# and - both condition must be true
# not - inverts the condition (not false, not true)


# temp=224
# is_raining = False

# if temp > 34 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# loops
# while loop is used to repeat a block od code as long as we receck the codition at the end

# if 1 ==1:
#  print("I am stuck in a loop!")   

# name=input("ENter your name")

# while name =="":
#     name=input("Enter your name:")
    
# age= int(input("Enter your age"))

# while age <0:
#     print("Age cannot be less than 0")
    
# print(f"Hello {name}")

# for loop is used to iterate over a sequence (sting, list ,tuple,set) rpeat a block of code an exact amount of times

# for i in range(1,1000):
#     print(i)

# name="Scarlett Johanson"

# for letter in name:
#     print(letter)

# list[] - mutable and most flexible
# tuple ()- immutable,faster
# set {} - mutable (add/remove), unordered,No duplicates,best for membership testing

# fruits=["Apple ","Orange ","Banana " , "Coconut "]
# print(fruits[2])
# fruits.append("Mango")

# find the largest number in the list

# numbers=[12,13,16,18,90]

# largest= max(numbers)

# print("Largest number :" , largest)

# check if a number is een or odd

# num = int(input("Enter a number : "))

# if num % 2 ==0:
#     print("Even")
# else:
#     print("Odd")

# Reverse a string

# text=input("Enter a string : ")

# reversed_text = text[:: -1]

# print("Reversed String:" , reversed_text)

# calculate factorial of a number

# num= int(input("ENter a number :"))

# factorial = 1

# for i in range(1, num + 1):
#     factorial *=i

#     print("Factorial :" , factorial)

#  check prime number

# num = int(input("ENter a number: "))

# if num > 1 :
#     for i in range(2,num):
#         if num %i ==0:
#             print("Not prime")
#             break
#         else:
#             print("Prime")
#     else:
#         print("Not prime")
    
# for i in range (1, 11):
#     print(i)
    
# for i in range(10, 0,-1):
#     print(i)

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x" , i, num * i)

# find the sum of numbers from 1 to n

# n=int(input("Enter n :"))
# total =0

# for i in range(1, n+1):
#     total += i

# print("Sum =" , total)

# find the factorial of a number

# n=int(input("Enter a number: "))
# fact= 1 

# for i in range(1,n +1):
#     fact *= i

# print("Factorial =" , fact)

# check if a number is positive

# num = int(input("Enter a number :"))
# if num >0:
#     print("Positive number")
    
    
# check if a number is positive or negative

# num = int(input("Enter a number :"))

# if num >0:
#     print("Positive")
# else:
#     print("Negative")

# check if a number is even or odd

# num=int(input("ENter a number :"))

# if num %2==0:
#     print("Even")
# else:
#     print("Odd")

# find the greatest of 2 number
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))

# if a > b :
#     print(a, "is greater")
# else:
#     print(b,"is greater")

# check if a person is eligible to vote

# age = int(input("Enter your age:"))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")

# check if a year is a leap year

# year =int(input("Enter a year :"))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100!= 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# check if a character is a vowel

# ch = input("Enter a character :")

# if ch.lower() in "aeiou":
#     print("Vowel")
# else:
#     print("Consonent")
    
# find the largest of 3 

# a= int(input())
# b= int(input())
# c= int(input())

# if a >=b and a >=c:
#     print(a, "is largest")
# elif b>= a and b >=c:
#     print(b,"is largest")
# else:
#     print(c,"is largest")

# check whether the number is divisible by  

# num=int(input("Enter a number:"))

# if num % 5==0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 5")

# check if a student passed

# marks = int(input("Enter marks:"))

# if marks >=40:
#     print("Pass")
# else:
#     print("Fail")

# marks= int(input("Enter marks :"))

# if marks >=90:
#     print("Grade A")
# elif marks >=75:
#     print("Grade B")
# elif marks >=60:
#     print("Grade C")
# elif marks >=40:
#     print("Grade D")
# else :
#     print("Fail")

# check if a number is divisible by both 3 and 5

# num=int(input("Enter number:"))

# if num % 3==0 and num %5==0:
#     print("Divisible by both")
# else:
#     print("Not divisible by both")

# find the absolute value

# num = int(input("ENter number :"))

# if num < 0:
#     print(-num)
# else:
#     print(num)

# check if a person is a senior citizen

# age=int(input("Enter age :"))

# if age >=60:
#     print("Senior citizen")
# else:
#     print("Not a senior citizen")

# check password

# password=int(input("Enter Password"))

# if password =="python1123":
#     print("Access granted")
# else:
#     print("Wrong password")
    
# check whether a number is a multiple of 10

# num=int(input("Enter number:"))

# if num % 10==0:
#     print("Multiple of 10")
# else:
#     print("Wrong password")

# check whether a number is between 1 and 100

# num = int(input("Enter number :"))

# if 1 <=num <=100:
#     print("Number is between 1 and 100")
# else:
#     print("outside the range ")

# find the smallest of 2 number 

# a = int(input())
# b=  int(input())

# if a < b :
#     print(a)
# else:
#     print(b)


# check if a person can get a driving license

# age=int(input("Enter age :"))
      
# if age >=18:
#     print("eligible for driving")
# else:
#     print("Not eligible")

# simple calculator using if-elif-else

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     print("Result =", a + b)
# elif op == "-":
#     print("Result =", a - b)
# elif op == "*":
#     print("Result =", a * b)
# elif op == "/":
#     if b != 0:
#         print("Result =", a / b)
#     else:
#         print("Division by zero is not allowed")
# else:
#     print("Invalid operator")

# check if number is positive , negative or zero

# num = int(input("Enter a number :"))

# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

# check if number is odd or even

# num = int(input("Enter a number :"))

# if num %2 ==0:
#     print("Even number")
# else:
#     print("Odd number")

# find the largest of 2 numbers

# a=int(input("Enter first number :"))
# b=int(input("Enter second number"))

# if a > b :
#     print(a, "is largest")
# else:
#     print(b, "is largest")

# find the largest of 2 numbers

# a=int(input("Enter first number :"))
# b=int(input("Enter second number"))

# if a > b :
#     print(a,"is largest")
# else:
#     print(b,"is largest")

# find largest of three number 

# a=int(input("Enter first number :"))
# b=int(input("Enter second number"))
# c=int(input("Enter third number"))

# if a >= b and a >=c:
#     print(a, "is largest")
# elif b >= a and b >=c:
#     print(b,"is largest")
# else:
#     print(c, "is largest")

# check voting eligibility

# age=int(input("Enter age :"))

# if age >=18:
#     print("Eligible to vote")
# else:
#     print("not eligible to vote")

# check leap year

# year = int(input("Enter a year :"))

# if (year % 400 ==0) or (year % 4 ==0 and year % 100!=0) :
#     print("Leap year")
# else :
#     print("Not leap year")

# create a list of fruit
# fruits =["Apple" , "Banana" ,"Mango","Orange"]

# print(fruits)

# acess list  elements

# numbers =[10,20,30,40,50]

# print("First element : ",
# numbers[0])

# print("Last element:")
# numbers[-1]

# add an element

# colors =["Red" , "Blue" , "Green"]

# colors.append("Yellow")
# print(colors)

# remove an element

# animals= ["Dog" , "Cat" , "Cow"]

# animals.remove("Cow")

# print(animals)

# update a list element

# cities =["Delhi" , "Mumbai" , "Pune"]
# cities[2] = "Jaipur"
# print(cities)

# find the length of a list

# languages = ["python" , "Java" ,"C" , "Javascript"]

# print("Length of list :" , len(languages))

# check if an item exists

# fruits = ["Apple" , "Banana" , "Mango"]

# if "Banana" in fruits:
#     print("Banana is present")
# else:
#     print("Banana is not present")

# sort a list

# numbers=[12,103,67,88,90]

# numbers.sort()

# print(numbers)

# reverse a list 

# numbers = [ 1,2 ,4,7,8]

# numbers.reverse()
# print(numbers)

# find the sum of list elements

# numbers = [1,2,3,6,7,8]

# total =sum(numbers)
# print("sum =" , total)

# create a tuple

# numbers=(10,20,30,40,50)
# print(numbers)

# access tuple elements

# colors=("Red" , "Blue" , "Yellow" , "Green")

# print("Second element :" , colors[1])
# print("Last element :" , colors[-1])

# find the length of tuple

# fruits =("Apple" , "Banana" , "Mango")

# print("Length of tuple :", len(fruits))

# check if an item exists in a tuple

# numbers =(10,20,30,40,50)

# if 20 in numbers:
#     print("20 is present")
# else:
#     print("20 is not present")

# count an element in a tuple

# numbers = (1,2,3,4,5,1,3,3)

# count = numbers.count(2)

# print("count of 3 =" , count)

# create a dictionary and print all key-value pair

# student= {
#     "name" : "Simran",
#     "age"  : 22,
#     "Course" : "Python"
# }

# student["city"] ="Delhi"
# student["age"] =23
# del student["city"]
# for key, value in student.items():
#     print(key, ":" , value)

# print(student["Course"])

# count the frequency of each character

# text ="Banana"

# frequency ={}

# for ch in text :
#     if ch in frequency:
#         frequency[ch] += 1
#     else :
#         frequency[ch] = 1
        
# print(frequency)

# find the highest value

# marks ={
#     "Math" : 90,
#     "English" : 85,
#     "Science" : 95
# }
# highest =max(marks.values())

# print(highest)

# merge two dictionaries

# d1= {
#     "a" : 1,
#     "b" :2
# }

# d2 = {
#     "c": 3,
#     "d": 4
# }

# d1.update(d2)
# print(d1)

# print only keys

# student={
#     "name" :"simran",
#     "age" :22,
#     "course":"Python"
# }

# for key in student.keys():
#     print(key)
    
# for value in student.keys():
#     print(value)

# create a set and print it

# numbers = {1,2,3,4,5}
# print(numbers)

# add an element to the set

# numbers = {1,2,3}
# numbers.add(4)
# print(numbers)

# remove an element

# numbers ={1,2,3,4}
# numbers.remove(2)
# print(numbers)

# find union of two sets

# set1 ={1,2,3}
# set2={4,5,6}

# result = set1.union(set2)

# print(result)

# find intersection

# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.intersection(set2))

# find difference 
# set1 ={1,2,3,4,5}
# set2={3,4}

# print(set1.difference(set2))

# check if an element exists

# numbers ={10,20,30,40,8}

# if 90 in numbers:
#     print("Found")
# else:
#     print("Not found")

# remove duplicate values

# numbers =[1,2,3,4,6,7,8,7,6,1,2,3]

# unique =set(numbers)

# print(unique)

# find symmetric difference

# set1 ={1,2,3}
# set2={3,4,5}

# print(set1.symmetric_difference(set2))

# clear all elements from a set

# numbers ={1,2,3,4}

# numbers.clear()

# print(numbers)

# i=1

# while i <=10:
#     print(i)
#     i +=1

# print numbers from 10 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -=1
    
# print even numbers from 1 to 20

# i = 2
# while i <= 20:
#     print(i)
# i +=2

# print odd numbets from 1 to 20

# i = 1

# while i <= 20:
#     print(i)
#     i += 2

# print the multplication table of a number

# numbers = int(input("ENter number :"))
# i = 1

# while i <= 10:
#     result = numbers* i

#     print(numbers, "x",i,"=",result)
#     i+=1

# def greet(name):
#     print("Hello" , name)
# greet("Simran")

# def add_numbers(a,b):
#     return a+b
# result=add_numbers(109,20)
# print("Sum :" , result)

# check whether a number is even or odd

# def check_even_odd(number):
#     if number %2==0:
#         print(number,"is even")
#     else:
#         print(number,"is odd")
        
# check_even_odd(2)
        
        
# find the largest of three numbers

# def find_largest(a,b,c):
#     if a >=b and a>=c:
#         return a
#     elif b >= a and b >=c:
#         return b
#     else:
#         return c
    
# largest = find_largest(120,13,14)
# print("Largest number :" , largest)

# calculate factorial of a number

# def factorial(number):
#     result = 1
    
#     for i in range(1, number + 1):
#         result=result*i

#     return result

# answer = factorial(5)
# print("Factorial:", answer)

# def say_hello():
#     print("Hello !")
# say_hello()

# def add(a,b):
#     result=a+b
#     print(result)
# add(2,1)

# print a person name

# def show_name(name):
#     print("My name is" , name)
    
# show_name("sneha")

# find the square of a number
# def square(number):
#     result=number*number
#     print(result)
# square(55)

# check if a number is positive

# def check_positive(number):
#     if number > 0:
#         print('Positive number')
#     else:
#         print('Not a positive number')
# check_positive(20)


# file= open("student.txt" ,"w")

# file.write("Name : Simran\n")
# file.write("Course : Data Science\n")
# file.write("Topic : Deep Learning\n")

# file.close()

# print("Data written successfully !")

# file=open("student.txt", "r")

# content=file.read()
# print(content)

# file.close()


# file=open("student.txt", "a")
# file.write("\nStatus : Learning Python ")

# file.close()

# print("Data added successfully")

# file=open("student.txt" , "r")

# for line in file:
#     print(line.strip())
# file.close()

# count the numbers of lines in a file

# file=open("student.txt" , "r")

# lines=file.readlines()

# print("Total lines:" , len(lines))
# file.close()

# file =open("student.txt","r")

# content =file.read()
# words=content.split()

# print("Total words:" , len(words))
# file.close()

# file =open("student.txt","r")

# content=file.read()
# word=input("Enter a word to search: ")

# if word.lower() in content.lower():
#     print("Word found")
# else:
#     print("Word not found")
    
# file.close()

# source=open("source.txt", "r")
# destination=open("destination.txt","w")

# content=source.read()
# destination.write(content)

# source.close()
# destination.close()

# print("File copied successfully !")

# file=open("source.txt" ,"r")

# content=file.read()

# print("total characters:" , len(content))
# file.close()

file=open("source.txt","w")
file.write("Hello Python")
file.close()

file=open("source.txt","r")
content=file.read()
print(content)
file.close()

file=open("source.txt","a")
file.write("\nI am learning Python")
file.close()

file=open("source.txt","r")
content=file.read()
print(content)
file.close()

file=open("source.txt","r")
line=file.readline()
print(line)
file.close()






