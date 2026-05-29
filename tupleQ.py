# question 1
# replace the last value of tuples in a list

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = [t[:-1] + (100,) for t in sample_list]

print(result)

# question 2
# remove empty tuples from a list of tuples

sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

result = [t for t in sample_data if t]

print(result)

# question 3
#sort a tuple by its float element

sample_data = [('item1', '12.20'),
               ('item2', '15.10'),
               ('item3', '24.5')]

result = sorted(sample_data, key=lambda x: float(x[1]), reverse=True)

print(result)

# question 4
#convert a tuple of positive integers into an integer

tuple1 = (1, 2, 3)
tuple2 = (10, 20, 40, 5, 70)

num1 = int(''.join(map(str, tuple1)))
num2 = int(''.join(map(str, tuple2)))

print(num1)
print(num2)

# question 5
# compute the sum of all elements of each tuple

list1 = [(1, 2), (2, 3), (3, 4)]
list2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

result1 = [sum(t) for t in list1]
result2 = [sum(t) for t in list2]

print(result1)
print(result2)

# question 6
# calculate the average value of numbers in a tuple of tuples

tuple1 = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

tuple2 = (
    (1, 1, -5),
    (30, -15, 56),
    (81, -60, -39),
    (-10, 2, 3)
)

result1 = [sum(x) / len(x) for x in zip(*tuple1)]
result2 = [sum(x) / len(x) for x in zip(*tuple2)]

print(result1)
print(result2)
