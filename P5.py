#1. Square of stars
for i in range(5):
    print("* " * 5)


#2. Right triangle of *
for i in range(1, 6):
    print("*" * i)


#3. Inverted triangle
for i in range(5, 0, -1):
    print("*" * i)


#4. Pyramid pattern
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)


#5. Number triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#6. Pattern of alphabets (A–E)
for i in range(65, 70):  # ASCII A=65
    print(chr(i) * (i - 64))


#7. Hollow square
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#8. Diamond pattern
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)


#9. Pattern using while loop
i = 1
while i <= 5:
    print("*" * i)
    i += 1


#10. Combine two patterns together
# Right triangle + inverted triangle
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)


#11. Arrow pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*")


#12. Half diamond
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)


#13. User-defined symbol pattern
symbol = "#"
for i in range(1, 6):
    print(symbol * i)


#14. Pascal’s triangle (basic)
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for k in range(i + 1):
        val = factorial(i) // (factorial(k) * factorial(i - k))
        print(val, end=" ")
    print()


#15. Butterfly pattern
n = 5
for i in range(1, n + 1):
    print("" * i + " " * (2 * (n - i)) + "" * i)
for i in range(n, 0, -1):
    print("" * i + " " * (2 * (n - i)) + "" * i)



