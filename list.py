# 1. Create an empty list called my_list.
my_list = []

# Print the initial empty list to show the starting point.
print(f"Initial list: {my_list}")

# 2. Append the elements 10, 20, 30, 40 to my_list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"After appending 10, 20, 30, 40: {my_list}")

# 3. Insert the value 15 at the second position (index 1).
my_list.insert(1, 15)

print(f"After inserting 15 at index 1: {my_list}")

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

print(f"After extending with [50, 60, 70]: {my_list}")

# 5. Remove the last element from my_list.
my_list.pop()

print(f"After removing the last element: {my_list}")

# 6. Sort my_list in ascending order.
my_list.sort()

print(f"After sorting the list: {my_list}")

# 7. Find and print the index of the value 30.
index_of_30 = my_list.index(30)
print(f"The index of the value 30 is: {index_of_30}")
