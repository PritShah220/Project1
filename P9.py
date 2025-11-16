# 1. Create a set
my_set = {1, 2, 3}
print("Initial set:", my_set)

# 2. Add elements
my_set.add(4)
my_set.update([5, 6])
print("After adding elements:", my_set)

# 3. Remove elements
my_set.remove(6)  # raises KeyError if not present
my_set.discard(5)  # no error if not present
print("After removing elements:", my_set)

# 4. Perform union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print("Union:", union_set)

# 5. Perform intersection
intersection_set = set1 & set2  # or set1.intersection(set2)
print("Intersection:", intersection_set)

# 6. Find difference
difference_set = set1 - set2  # or set1.difference(set2)
print("Difference:", difference_set)

# 7. Check if subset or superset
print("Is set1 subset of set2?", set1.issubset(set2))
print("Is set2 superset of set1?", set2.issuperset(set1))

# 8. Clear all elements
set1.clear()
print("Set1 after clear:",set1) 
