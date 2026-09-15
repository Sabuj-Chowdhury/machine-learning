# for - loop 
# range() acepts 3 things (start,stop,step)
# for i in range(1,20):
#     print(i)

# reverse for-loop
# for i in range(16,0,-1):
#     print(i)

# print a table of 5
# num=5 
# for i in range(1,11):
#     result = num * i
#     print(f"{num} * {i} = {result} ")

# accept an integer and print hello world n times
# n=int(input("how many times :"))
# for i in range(n):
#     print("Hello world.")

# print natural number up to n
# n=int(input("n :"))
# for i in range(1,n+1):
#     print(i)
# reverse for-loop n to 1
# n=int(input("n :"))
# for i in range(n,0,-1):
#     print(i)
# sum upto n terms
# n= int(input("n :"))
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print(f"sum is = {sum}")

# factorial of a number
# n= int(input("n :"))
# fact = 1
# for i in range(1,n+1):
#     fact *=i
    
# print(f"factorial = {fact}")

# even and odd both number sum
# n = int(input("n :"))
# even = 0
# odd = 0

# for i in range(0,n+1):
#     if(i % 2 == 0):
#         even+=i
#     else:
#         odd+=i
        
# print(f"total odd = {odd} and even = {even}")

# print all the factors of a number
# n = int(input("n :"))

# for i in range(1,n+1):
#     if(n % i == 0):
#         print(i)

# accept a number, check if it's a perfect number or not
# n = int(input("n :"))
# sum = 0
# for i in range(1,n):
#     if(n % i == 0):
#         sum+=i
# if(sum == n):
#     print("perfect numer")
# else:
#     print("not perfect number")

# check wheather a number is prime or not 
# n = int(input("n :"))
# count = 0
# for i in range(1,n+1):
#     if(n % i == 0):
#         count+=1
# if(count == 2):
#     print("prime number")
# else:
#     print("not a prime number")

# reverse a string without any in built methods
# name = input("name : ")

# reverse = ""

# for char in range(len(name)-1,-1,-1):
#     reverse+=name[char]
# print(reverse)

# palindrom or not 
# name = input("name :")

# reverse = ""

# for char in range(len(name)-1,-1,-1):
#     reverse = reverse + name[char]

# if(reverse == name):
#     print(f"{name} is palindrom")
# else:
#     print(f"{name} is not a palindrom")
    
# count all letter,digits and special charecters in a given string
# string = input("string :")
# char = 0
# spChar = 0
# digits = 0

# for i in string:
#     if i.isdigit():
#         digits = digits + 1
#     elif i.isalpha():
#         char = char + 1
#     else:
#         spChar = spChar + 1

# print(f"{digits} , {char} , {spChar}")