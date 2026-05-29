# Question 1 soln

def first_three(text):
    if len(text) < 3:
        return text
    return text[:3]


print(first_three("war"))


# Question 2 soln
# Write a python program to create a Ceasar encryption

def caesar_encrypt(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')

            else:
                start = ord('a')

            encrypted_char = chr((ord(char) - start - shift) % 26 + start)

            result += encrypted_char

        else:
            result += char

    return result


message = input("Enter a message: ")
shift_value = int(input("Enter shift value: "))

encrypted_message = caesar_encrypt(message, shift_value)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)



# Question 3
# Write a Python program to remove duplicate characters from a given string.

def remove_duplicates(text):

    result = ""

    for char in text:

        if char not in result:
            result += char

    return result


word = "programming"

new_word = remove_duplicates(word)

print("Original String:", word)
print("After Removing Duplicates:", new_word)

# question 4
# program to delete all occurrences of a specified char

# Original string
text = "Delete all occurrences of a specified character in a given string"

# Character to remove
char_to_remove = "a"

# Remove all occurrences of the character
modified_text = text.replace(char_to_remove, "")

# Print results
print("Original string:")
print(text)

print("\nModified string:")
print(modified_text)

#Quesrtion 5
# Function to count leap years in a given range

def count_leap_years(year_range):
    
    start, end = map(int, year_range.split("-"))
    
    count = 0

    for year in range(start, end + 1):

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count += 1

    return count


print(count_leap_years("1981-1991"))  
print(count_leap_years("2000-2020"))  

#Question 6
# Function to insert spaces before capital letters

def insert_spaces(word):
    
    result = ""

    for char in word:
        
        # Add space before uppercase letters (except the first character)
        if char.isupper() and result:
            result += " "

        result += char

    return result


# Sample Data
print(insert_spaces("PythonExercises"))
print(insert_spaces("Python"))
print(insert_spaces("PythonExercisesPracticeSolution"))
