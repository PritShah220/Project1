 x# 1. Perform all arithmetic operations on two numbers
a = 10
b = 3
print("1. Arithmetic Operations:") 
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)
print("-" * 50) 

# 2. Usage of assignment operators
print("2. Assignment Operators:")
x = 5
x += 3
x -= 2
x *= 4
x /= 2
print("Final value of x:", x)
print("-" * 50)

# 3. Logical operators with boolean values
print("3. Logical Operators:")
p, q = True, False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print("-" * 50)

# 4. Comparison operators
print("4. Comparison Operators:")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("-" * 50)

# 5. Bitwise operators
print("5. Bitwise Operators:")
print("a & b (AND):", a & b)
print("a | b (OR):", a | b)
print("a ^ b (XOR):", a ^ b)
print("~a (NOT):", ~a)
print("a << 1 (Left Shift):", a << 1)
print("a >> 1 (Right Shift):", a >> 1)
print("-" * 50)

# 6. Membership operators
print("6. Membership Operators:")
nums = [1, 2, 3, 10]
print("Is 10 in nums?", 10 in nums)
print("Is 5 not in nums?", 5 not in nums)
print("-" * 50)

# 7. Identity operators
print("7. Identity Operators:")
x = [1, 2]
y = x
z = [1, 2]
print("x is y:", x is y)
print("x is not z:", x is not z)
print("-" * 50)

# 8. Expression combining multiple operators
print("8. Combined Expression:")
result = (a + b) * 2 - (a / b)
print("Result:", result)
print("-" * 50)

# 9. Remainder and quotient
print("9. Remainder and Quotient:")
print("Quotient:", a // b)
print("Remainder:", a % b)
print("-" * 50)

# 10. Compound Interest Calculation
print("10. Compound Interest:")
principal = 1000
rate = 5
time = 2
CI = principal * ((1 + rate / 100) ** time) - principal
print("Compound Interest:", CI)
print("-" * 50)

# 11. Area of a triangle
print("11. Area of a Triangle:")
base = 10
height = 5
area = 0.5 * base * height
print("Area:", area)
print("-" * 50)

# 12. Evaluate (a + b)**2
print("12. Complex Expression:")
expr = (a + b) ** 2
print("(a + b)^2 =", expr)
print("-" * 50)

# 13. Augmented assignment example
print("13. Augmented Assignment:")
x = 10
x += 10
print("x after += 10:", x)
print("-" * 50)

# 14. BMI Calculator
print("14. BMI Calculator:")
weight = 70  # in kg
height_m = 1.75  # in meters
BMI = weight / (height_m ** 2)
print("BMI:", round(BMI, 2))
print("-" * 50)

# 15. Using pow() and abs()
print("15. pow() and abs() demonstration:")
num = -4
power_val = pow(num, 2)
abs_val = abs(num)
print("pow(-4, 2):", power_val)
print("abs(-4):", abs_val)
print("-" * 50)