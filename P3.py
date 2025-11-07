#1. Check if a number is positive or negative
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



#2. Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)



 #3. Check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



#4. Simple grading system
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")



# 5. Divisible by both 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")



# 6. Leap year check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")



# 7. Voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# 8. Vowel or consonant
ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")



# 9. Login credentials check
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")



# 10. Nested if eligibility check
age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()
if age >= 18:
    if citizen == "yes":
        print("Eligible")
    else:
        print("Not a citizen")
else:
    print("Too young")



# 11. Smallest of three numbers
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
if a <= b and a <= c:
    print("Smallest:", a)
elif b <= a and b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)



# 12. Temperature alert system
temp = float(input("Enter temperature: "))
if temp > 40:
    print("Heat alert!")
elif temp > 30:
    print("Warm weather")
elif temp > 20:
    print("Pleasant")
else:
    print("Cold")



# 13. Use of pass in if statement
num = int(input("Enter a number: "))
if num < 0:
    pass  # Placeholder for future logic
else:
    print("Positive number")



# 14. Check if a number is zero
num = float(input("Enter a number: "))
if num == 0:
    print("Zero")
else:
    print("Non-zero")



# 15. Menu-based calculator
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Choose operation (1-4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")


