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
s={9,9.0,"9"}
print(s)