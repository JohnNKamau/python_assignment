# question 1
#python program to find the length of a set
my_set = {1, 2, 3, 4, 5}
length = len(my_set)
print(f"Length of the set: {length}")

#question 2
#python program to add member to a set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(f"Set after adding member: {my_set}")

#question 3
#python program to remove items from a given set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(f"Set after removing item: {my_set}")

#question 4
#python program to create an intersection of sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print(f"Intersection of sets: {intersection}")

#question 5
#python program to create a union of sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print(f"Union of sets: {union}")

#question 6
#python program to create a set difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
difference = set1.difference(set2)
print(f"Difference of sets: {difference}")

#question 7
#python program to find the maximum and minimum value in a set
my_set = {3, 1, 4, 1, 5, 9}
max_value = max(my_set)
min_value = min(my_set)
print(f"Maximum value in the set: {max_value}")
print(f"Minimum value in the set: {min_value}")