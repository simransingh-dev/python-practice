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

# num = 10

# if num >0:
#     print("Positive number")
 
# num=-5
# if num>0:
#      print("Negative number")

# check if a number is zero

# num = 0
# if num ==0:
#     print("The number is zero")

# check if a number is even
# num=8
# if num%2==0:
#     print("Even number")

# num=7
# if num%2==0:
#     print("Odd number")

# age=20

# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# age=22

# if age >=18:
#     print("Adult")
# else:
#     print("Minor")

# check whether 2 numbers are equal

# a=10
# b=100

# if a == b :
#     print("Both numbers are equal")
# else:
#     print("Numbers are not equal")

# a=20
# b=15

# if a > b:
#     print("a is grater")
# else:
#     print("b is greater")

# a=5
# b=9

# if a < b:
#     print("A is smaller")
# else:
#     print("B is smaller")

# check if a number is greater than 100

# num = 150

# if num>100:
#     print("Greater than 100")
# else:
#     print("Not greater than 100")

# num=25

# if num % 5==0:
#     print("divisible by 5")
# else:
#     print("Not divisible by 5")

# num=60

# if num%10==0:
#     print("Divisible by 10")
# else:
#     print("Not divisible by 10")

# num=15

# if num %3==0 and num%5==0:
#     print("divisible by both")
# else:
#     print(" not divisible by both")

# num = 9

# if num%2==0 or num%3==0:
#     print("divisible by 2 or 3")
# else:
#     print(" not divisible by both")

# check whether the character is a vowel

# char = "a"

# if char in "aeiouAEIOU":
#     print("Vowel")
# else:
#     print("Not vowel")

# char ="b"

# if char not in "aeiouAEIOU":
#     print("Consonent")
# else:
#     print("Vowel")

# check whether a password is correct

# password="Python123"

# if password =="Python123":
#     print("Correct Password")
# else:
#     print("Incorrect password")

# check whether a username is correct

# username="Simran"

# if username=="Simran":
#     print("Valid username")
# else:
#     print("Invallid username")
    
# check username and password together

# username="simran"
# password="1234"

# if username =="simran" and password=="1234":

#     print("login successful")
# else:
#     print("Invalid crediantials")

# check whether marks represent a pass or fail

# marks=45
# if marks >=33:
#     print("Pass")
# else:
#     print("Fail")

# assign a grade based marks

# marks = 85

# if marks >=90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 75:
#     print("Grade C")
# elif marks >= 75:
#     print("Grade D")
# else:
#     print("Fail")

# check whether the temperature is cold or not

# temperature = 32

# if temperature > 25:
#     print("Hot")
# else:
#     print("Cold")


# check whether it is morning,evening or afternoon

# hour=15

# if hour <12:
#     print("Morning")
# elif hour < 18:
#     print("afternoon")
# else:
#     print("Evening")

# check whether the number has one two or three digit

# num = 75

# if num <10:
#     print("One digit")
# elif num < 100:
#     print("Two digit")
# else:
#     print("Three or more digits")

# find the largest of three numbers

# a=10
# b=25
# c=15

# if a >=b and a >=c:
#     print("a is largest")
# elif b >=a and b >=c:
#     print("b is largest")
# else:
#     print("C is largest")

# find the smallest of three numbers

# a = 100
# b=12
# c=90

# if a <= b and a <=c:
#     print("a is smallest")
# elif b <=a and b<=c:
#     print("B is smallest")
# else:
#     print("C is smallest")

# check whether a leap is a leap year

# year = 2024

# if year % 400==0:
#     print("Leap year")
# elif year % 100==0:
#     print("nOt a leap year")
# elif year %4==0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# check whether a number is between 0 and 1 

# num = 7
# if num <=num<=10:
#     print("number is betwwen 1 and 10")
# else:
#     print("number is outside the range")

# check whethe rthe number is outside the range 1 and 100

# num = 10

# if num <1 or num> 100:
#     print("outsid ethe range")
# else:
#     print("Inside the range")

#  check if a person can drive

# age=20

# if age >=18:
#     print("Can drive")
# else:
#     print("Cannot drive")

# check ticket price based on age

# age =12

# if age <5:
#     print('Free ticket')
# elif age <18:
#     print("Child ticket")
# else:
#     print("Adult ticket")

# check whether  anumber is positive, negative or 0

# num=8

# if num > 0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")

# check whether the number is even or odd
# num=11

# if num %2==0:
#     print("Even")
# else:
#     print("odd")

# check whether the person is child, teenage or adult
# age = 16

# if age <13:
#     print("Child")
# elif age <18 :
#     print("Teenager")
# else:
#     print("Adult")

# check whether a number is multiple of 7

# num=49

# if num %7==0:
#     print("Multiple of 7")
# else:
#     print('not a multiple of 7')

# check if a shopping qualifies for a discount

# amount=1000

# if amount >=10000:
#     print("discount available")
# else:
#     print("not available")

# check if a student is eligible for an exam

# attendance = 80

# if attendance >=75:
#     print("Eligible for an exam")
# else:
#     print("Not eligible for an exam")

# check if a number is both positive and even
# num=12
# if num > 0 and num%2==0:
#     print('Positive and even')
# else:
#     print("Condition not satisfied")

# check if number is negative or odd

# num=12
# if num <0 and num % 2!=0:
#     print("negative and odd")
# else:
#     print("condition not satisified")

# check whether a letter is lowercase

# char="A"

# if char.isupper():
#     print("Uppercase")
# else:
#     print("not uppercase")

# check whether a letter is lowercase

# char="a"

# if char.islower():
#     print("Lowercase")
# else:
#     print("Not lowercase")

# check whether the string is empty

# text=""
# if text =="":
#     print("String is empty")
# else:
#     print("String is not empty")

# check whether the list is empty

# number=[]

# if len(number)==0:
#     print('list is empty')
# else:
#     print("List is not empty")

# check whether a number exists in a list

# numbers=[10,20,30,40,50]
# num=20

# if num in numbers:
#     print("Number found")
# else:
#     print("not found")

# checl traffic light instructions

# light = "Red"

# if light =="Red":
#     print("Stop")
# elif light =="yellow":
#     print("Wait")
# elif light =="Green":
#     print("Go")
# else:
#     print("invalid signal")

# check day type

# day ="Sunday"
# if day=="Saturday"or day=="Sunday":
#     print("weekend")
# else:
#     print("Weekday")

# check whether three sides form a triangle

# a=3
# b=4
# c=1

# if a +b>c and a+c>b and b +c>a:
#     print("valid triangle")
# else:
#     print("invalid triangle")

# check whether a person qualifies for a loan based on age and salary

# age=25
# salary=30000

# if age >=21 and salary>=25000:
#     print("Eligible for a loan")
# else:
#     print("Not eligible for loan")

# create a simple calculator using conditionals

# a=10
# b=5
# operator="+"

# if operator =="+":
#     print(a+b)
# elif operator =="-":
#     print(a-b)
# elif operator =='*':
#     print(a*b)
# elif operator =="/":
#     print(a/b)
# else:
#     print("invalid operator")

# num=int(input("ENter a number :"))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# check even or odd

# num=int(input("ENter a number :"))
# if num %2==0:
#     print("EVen")
# else:
#     print("Odd")
 # checking voting eligibility

# age=int(input("ENter your age :"))

# if age >=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# find greatest of two numbers

# a=int(input("ENter first number :"))
# b=int(input("ENter second number:"))

# if a>b:
#     print(a,"is greater")
# elif b>a:
#     print(b,"is greater")
# else:
#     print("Both numbers are equal")

# check divisibility by 5

# num=int(input("ENter a number :"))

# if num %5 ==0:
#     print("DIvisible by 5")
# else:
#     print("Not divisible by 5")

# check divisibility by both 3 and 5

# num=int(input("Enter a number :"))

# if num %3==0 and num%5==0:
#     print("divisible by both")
# else:
#     print("Not divisible")

# check leap year

# year=int(input("Enter a year :"))

# if year %400==0:
#     print("Leap year")
# elif year %100==0:
#     print("not a leap year")
# elif year %4==0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# check vowel or consonent

# char=input("Enter a character :").lower()
# if char in "aeiou":
#     print("Vowel")
# else:
#     print("consonent")

# find the largest of three numbers

# a=int(input("Enter first number :"))
# b=int(input("Enter second number :"))
# c=int(input("Enter third number :"))

# if a >=b and a >=c:
#     print(a,"is largest")
# elif b >=a and b >=c:
#     print(b,"is largest")
# else:
#     print(c,"is largest")

# find smallest of three numbers

# a=int(input("Enter first number :"))
# b=int(input("Enter second number :"))
# c=int(input("Enter third number :"))

# if a <=b and a<=c:
#     print(a,"Is smallest")
# elif b <=a and b<=c:
#     print(b,"Is smallest")
# else:
#     print(c,"is smallest")

# checking driving eligibility

# age=int(input("Enter your age :"))

# if age >=18:
#     print("Eligible to drive")
# else:
#     print("Not eligible to drive")
    
# check whether a number is multiple of 10

# num=int(input("Enter a number :"))

# if num %10==0:
#     print("Multiple of 10")
# else:
#     print("Not multiple of 10")

# check uppercase or lowercase

# char=input("Enter a character:")

# if char.isupper():
#     print("Uppercase")
# elif char.islower():
#     print("Lowercase")
# else:
#     print("Not an alphabet")


# grade calculator

# marks=float(input("Enter your marks:"))

# if marks >=90:
#     print("GRade A")
# elif marks >=80:
#     print("Grade B")
# elif marks >=70:
#     print("Grade C")
# elif marks>=60:
#     print("Grade D")
# else:
#     print("Grade F")

# check pass or fail

# marks=float(input("Enter marks:"))
# if marks >=40:
#     print("Pass")
# else:
#     print("Fail")

# check number range

# num=int(input("Enter a number :"))

# if 1<= num <=100:
#     print("Number is between 1 and 100")
# else:
#     print("Number is outisde the range")


# check teenager 

# age=int(input("Enter your age :"))

# if 13 <= age <=19:
#     print("Teenager")
# else:
#     print("Not a teenager")

# simple login system

# username=input("Enter username:")
# password =input("Enter password:")

# if username =="admin" and password=="1234":
#     print("Login successful")
# else:
#     print("Invalid username or password")

# check alphabet , digit or special character

# char=input("Enter a charater")

# if char.isalpha():
#     print("Alphabet")
# elif char .isdigit():
#     print("Digit")
# else:
#     print("Special character")

# check divisibility  by 2 or 3

# num=int(input("Enter a number :"))

# if num %2==0 and num%3==0:
#     print("Divisible by 2 or 3")
# else:
#     print("Not divisible")

# temperature = float(input("Enter temperature:"))

# if temperature <10:
#     print("Cold")
# elif temperature<=25:
#     print("Moderate")
# else:
#     print("Hot")

# age category

# age=int(input("Enter your age:"))

# if age <13:
#     print("Child")
# elif age <20:
#     print("Teenager")
# elif age <60:
#     print("Adult")
# else:
#     print("Senior citizen")

# check three digit number

# num=int(input("Enter a number :"))

# if 100 <=abs(num) <=999:
#     print("Three digit number")
# else:
#     print("Not a three digit number")

# check whether last digit is 5
# num=int(input("Enter an number :"))

# if abs(num) % 10 ==5:
#     print("Last digit is 5")
# else:
#     print("Last digit is not")

# check number sign and parity

# num=int(input("EWnter a number :"))

# if num >0:
#     if num %2==0:
#         print("Positive and even")
#     else:
#         print("Positive and odd")
# elif num <0:
#     if num % 2==0:
#         print("Negative and even")
#     else:
#         print("Negative and odd")
# else:
#     print("Zero")

# calculate discount 

# amount=float(input("Enter purchase amount :"))
# if amount >=1000:
#     discount=amount*0.10
#     final_amount=amount-discount
# else:
#     final_amount=amount

# print("Final amount:", final_amount)

# Salary bonus calculator

# salary=float(input("Enter salary:"))
# years=int(input("Enter yuears of service:"))

# if years>=5:
#     bonus=salary*0.10
# else:
#     bonus=0
    
# print("Bonus :" ,bonus)

# electricity bill calculator

# units=int(input("enter electricity units:"))

# if units<=100:
#     bill=units*5
# elif units<=200:
#     bill=100*5 +(units-100)*7
# else:
#     bill=100*5 + 100*7+(units-200) *10
    
# print("ELectricity bill",bill)

# bmi category
# weight=float(input("ENter weight in kg :"))
# height=float(input("Enter height in meters :"))

# bmi=weight /(height **2)

# if bmi < 18.5:
#     print("Underweight")
# elif bmi<25:
#     print("Normal weight")
# elif bmi <30:
#     print("Overweight")
# else:
#     print("Obese")

# check valid traingle

a=float(input("Enter first side:"))
b=float(input("ENter second side:"))
c=float(input("Enter third side :"))

if a+b >c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")