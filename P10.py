# 1. Create a dictionary of student details
student = {"name": "Alice", "age": 20, "course": "Computer Science"}
print("Initial dictionary:", student)

# 2. Access and modify values
print("Student name:", student["name"])
student["age"] = 21  # modify age
print("Modified age:", student["age"])

# 3. Add new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# 4. Delete a key from dictionary
del student["grade"]
print("After deleting grade:", student)

# 5. Print all keys and values separately
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

# 6. Check if key exists
print("Is 'course' a key?", "course" in student)

# 7. Use get() method
print("Get course:", student.get("course"))
print("Get phone (default None):", student.get("phone"))

# 8. Iterate using .items()
print("Iterate over items:")
for key, value in student.items():
    print(f"{key}: {value}")

# 9. Copy a dictionary
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# 10. Merge two dictionaries
extra_info = {"phone": "123456789", "email": "alice@example.com"}
student.update(extra_info)
print("After merging:", student)

# 11. Create nested dictionary
students = {
    "001": {"name": "Alice", "age": 21},
    "002": {"name": "Bob", "age": 22}
}
print("Nested dictionary:", students)

# 12. Use dictionary comprehension
squared = {x: x*x for x in range(1, 6)}
print("Dictionary comprehension:", squared)

# 13. Sort dictionary by keys
sorted_dict = dict(sorted(student.items()))
print("Sorted dictionary by keys:", sorted_dict)

# 14. Find maximum value from dictionary (assuming values are comparable)
marks = {"Alice": 88, "Bob": 92, "Charlie": 87}
max_score = max(marks.values())
print("Maximum value:", max_score)

# 15. Count word frequency from sentence
sentence = "this is a test this is only a test"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)



