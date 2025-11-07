#1. Take input and print string length
s = input("Enter a string: ")
print("Length:", len(s))


#2. Convert string to uppercase & lowercase
s = "Hello World"
print(s.upper())
print(s.lower())


#3. Reverse a string using slicing
s = "Python"
print(s[::-1])


#4. Count vowels in a string
s = "Programming"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print("Vowel count:", count)


#5. Check palindrome string
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


#6. Replace a word in a sentence
s = "I love apples"
print(s.replace("apples", "bananas"))


#7. Find substring position
s = "Hello World"
pos = s.find("World")
print("Position:", pos)


#8. Split and join words
s = "Learn Python Programming"
words = s.split()
joined = "-".join(words)
print("Split:", words)
print("Joined:", joined)


#9. Remove spaces from a string
s = "  Hello   World  "
print(s.replace(" ", ""))


#10. Count frequency of each character
s = "banana"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)


#11. Check if string is alphanumeric
s = "Python123"
print(s.isalnum())


#12. Convert string to list of characters
s = "Code"
char_list = list(s)
print(char_list)


#13. Swap case of string
s = "PyThOn"
print(s.swapcase())


#14. Print each character using loop
s = "Loop"
for char in s:
    print(char)


#15. Concatenate two strings with formatting
s1 = "Hello"
s2 = "World"
print(f"{s1}, {s2}!")

