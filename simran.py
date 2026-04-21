name = input("Enter your name: ")
print("Hello", name + ", welcome to Python!")



# 2. Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)



# 3. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# 4. Largest of Two Numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print(x, "is greater")
else:
    print(y, "is greater")



# 5. Swap Two Numbers (without third variable)
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

p, q = q, p

print("After swapping:")
print("p =", p)
print("q =", q)


# 6. Square and Cube
n = int(input("Enter a number: "))
print("Square:", n ** 2)
print("Cube:", n ** 3)


# 7. Simple Interest
P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time: "))

SI = (P * R * T) / 100
print("Simple Interest:", SI)



# 8. Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)