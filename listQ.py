# Question 1
#first and last 5 elements where the values are square numbers between 1 and 30

squares = [x**2 for x in range(1, 31) if x**2 <= 30]

print("Square numbers:", squares)
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])


# Question 2

#Difference between 2 lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

difference = list(set(list1) - set(list2))

print("Difference between lists:", difference)

# Question 3
#Concatenate a given list with a range form 1 to n

sample_list = ['p', 'q']
n = 5

result = [item + str(i) for i in range(1, n + 1) for item in sample_list]

print(result)

# Question 4
# Convert a list to a list of dictionaries

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = [
    {"color_name": name, "color_code": code}
    for name, code in zip(color_names, color_codes)
]

print(result)

#Question 5
# python program to move all zero digits to the end of a given list of numbers

numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0,
           9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# Separate non-zero and zero elements
non_zero = [num for num in numbers if num != 0]
zeros = [num for num in numbers if num == 0]

result = non_zero + zeros

print("Original list:")
print(numbers)

print("Move all zero digits to end:")
print(result)

#Question 6
# Round Numbers, Find Min/Max, Multiply by 5, and Print Unique Values

numbers = [22.4, 4.0, 16.22, 9.1, 11.0,
           12.22, 14.2, 5.2, 17.5]

rounded = [round(num) for num in numbers]

minimum = min(rounded)
maximum = max(rounded)

multiplied = [num * 5 for num in rounded]

unique_values = sorted(set(multiplied))

print("Original list:")
print(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)

print("Result:")
print(*unique_values)

# Question 7
#count the number of lists in a list of lists

list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]

count = len(list1)

print("Original list:")
print(list1)

print("Number of lists in said list of lists:")
print(count)