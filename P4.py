            #This is looping Statement Projects 

#1. Print numbers from 1 to 10 using for  
for i in range(1, 11):
    print(i)


#2. Print even numbers from 1 to 50 using while
i = 2
while i <= 50:
   print(i)
   i += 2  


#3. Calculate the sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)


#4. Print multiplication table of any number
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#5. Display numbers divisible by 3 between 1–100
for i in range(1, 101):
    if i % 3 == 0:
        print(i)


#6. Reverse a number using a loop
num = 12345
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)


#7. Find factorial of a number using for
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)


#8. Calculate the sum of digits in a number
num = 1234
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)


#9. Use break to stop a loop at 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)


#10. Use continue to skip 3 in a loop
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


#11. Print a countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)


#12. Find prime numbers from 1–50
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


#13. Print Fibonacci series up to 10 terms
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b


#14. Nested loop to print pairs (i, j)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})")


#15. Use range() function creatively
# Print squares of even numbers from 2 to 20
for i in range(2, 21, 2):
    print(f"{i}^2 = {i**2}")


