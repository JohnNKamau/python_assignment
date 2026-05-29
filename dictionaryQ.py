#question1 solution
# pythhon script to concantenate dictionaries to create a new one
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
def dictconca(dict1, dict2, dict3):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    new_dict.update(dict3)
    return new_dict
final_dict = dictconca(dict1, dict2, dict3)
print(f"Concatenated dictionary: {final_dict}")

#method 2
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
final_dict = dict1 | dict2 | dict3
print(f"Concatenated dictionary: {final_dict}")

# question 2 solution
#python program to print all distinct values in a dictionary
my_dict = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
distinct_values = set()
for d in my_dict:
    distinct_values.update(d.values())
print(f"Distinct values in the dictionary: {distinct_values}")  

# question 3 solution
#python program to combine two dictionary by adding values for common keys
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
def combineDictionaries(dict1, dict2):
    combined_dict = dict1.copy()
    for key, value in dict2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value
    return combined_dict
final_dict = combineDictionaries(dict1, dict2)
print(f"Combined dictionary: {final_dict}")

#question 4 solution
#python program to get the top three items in a shoping dictionary with expected output as item4 55 item1 45.5 item3 41.3
shopping_dict = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24.0}
top_items = sorted(shopping_dict.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top three items in the shopping dictionary:")
for item, price in top_items:
    print(f"{item}: {price}") 

#question 5 solution
#python program to filter a dictionary based on values
my_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
threshold = 170

filtered_dict = {}

for value in my_dict:
    if my_dict[value] > threshold:
        filtered_dict[value] = my_dict[value]

print("Filtered dictionary with values greater than 170:", filtered_dict)

#question 6 solution
#python program to extract a list of values from a given list of dictionaries whereby the orignl dictionarry is as follows [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]with expected output as [92, 94, 88]
# and the other original dictionary is as follows [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}] with expected output as [90, 89, 92]
list_of_dicts = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
science_scores = [d['Science'] for d in list_of_dicts]
math_scores = [d['Math'] for d in list_of_dicts]
print(f"Science scores: {science_scores}")
print(f"Math scores: {math_scores}")