#Create a list of 5 numbers and print it.

# numbers = [10, 20, 30, 40, 50]

# # Print the list
# print(numbers)

## Create a list of 5 numbers
# numbers = [10, 20, 30, 40, 50]

# # Calculate the sum of the list elements
# total_sum = sum(numbers)

# Calculate the average of the list elements
# average = total_sum / len(numbers)

# # Print the results
# print("Sum:", total_sum)
# print("Average:", average)

#Add and remove elements from a list.
#Create a list
numbers = [10, 20, 30, 40, 50]

# Add elements
numbers.append(60)        # Add 60 at the end
numbers.insert(2, 25)     # Insert 25 at index 2
numbers.extend([70, 80])  # Add multiple elements

print("After additions:", numbers)  # [10, 20, 25, 30, 40, 50, 60, 70, 80]

# Remove elements
numbers.remove(25)        # Remove first occurrence of 25
popped = numbers.pop(3)   # Remove element at index 3 (30)
numbers.clear()           # Remove all elements

print("Popped element:", popped)    # 30
print("After removals:", numbers)   # []

#7.Sort list in ascending and descending order
numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

# Sort in ascending order (default)
numbers.sort()
print("Ascending:", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("Descending:", numbers)

# Using sorted() to get a new sorted list without changing original
numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]
asc_sorted = sorted(numbers)
desc_sorted = sorted(numbers, reverse=True)

print("Original list:", numbers)
print("Ascending using sorted():", asc_sorted)
print("Descending using sorted():", desc_sorted) 

#8.find maximum and minimum elements. 
numbers = [10, 20, 5, 40, 15]

max_num = max(numbers)  # Finds the maximum element
min_num = min(numbers)  # Finds the minimum element

print("Maximum element:", max_num)
print("Minimum element:", min_num)

numbers = [10, 20, 10, 40, 10, 50, 20]

# 9.Count occurrences of the number 10
count_10 = numbers.count(10)

print("Occurrences of 10:", count_10)


numbers = [10, 20, 30, 40, 50]

# 10.Reverse the list using slicing
reversed_numbers = numbers[::-1]

print("Original list:", numbers)
print("Reversed list:", reversed_numbers)

numbers = [10, 20, 30, 40, 50]

# 11.Check if 30 exists in the list
exists = 30 in numbers
print("30 exists:", exists)

# Check if 60 exists in the list
exists = 60 in numbers
print("60 exists:", exists)

#Copy a list to another variable.
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print(original_list) 

#12remove duplicate values 
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # Output: [1, 2, 3, 4, 5, 6]

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)  # Output: ['a', 'b', 'c']

#13.Find the index of an element.

numbers = [10, 20, 30, 40, 50, 30]

# Find the index of the first occurrence of 30
index_30 = numbers.index(30)

print("Index of 30:", index_30)

numbers = [1, 2, 3, 4, 5]

# 14.Square each number using list comprehension
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# 15.Create a 2D list (3x3 matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#. Access elements: row 1, column 2 (indexing starts from 0)
element = matrix[1][2]  # This gets the element '6'

print("Element at row 2, column 3:", element)






