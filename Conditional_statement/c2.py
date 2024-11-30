# Practical Example 6: Write a Python program to check if a number is prime using if_else.

num = int(input("Enter any number:"))
count=0
if num>1:
    for i in range(2,num):
        if num % i == 0:
            count +=1
if count==0:
    print(f"{num} is a prime number") 
else:
    print(f"{num} is not prime number")
