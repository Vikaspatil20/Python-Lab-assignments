#
#Vikas Patil
#Python Lab Assignment - 9
#


1.Write a Python program to Count all letters, digits, and special symbols from the given string
  Input = “P@#yn26at^&i5ve” 

Program:

# Input string
input_string = "P@#yn26at^&i5ve"

# Count letters, digits, and special symbols
letters = sum(c.isalpha() for c in input_string)
digits = sum(c.isdigit() for c in input_string)
special_symbols = len(input_string) - letters - digits

# Print results
print(f"Chars: {letters}")
print(f"Digits: {digits}")
print(f"Symbols: {special_symbols}")


Output: 

Chars: 8
Digits: 3
Symbols: 4



2.Write a Python program to remove duplicate characters of a given string.
  Input = “String and String Function” 
  Output: String and Function 

Program:

from collections import OrderedDict

def remove_duplicate_words(input_string):
    # Split the string into words and use OrderedDict to remove duplicates while maintaining order
    unique_words = OrderedDict.fromkeys(input_string.split())
    return " ".join(unique_words)

# Example usage
input_string = "String and String Function"
output = remove_duplicate_words(input_string)
print("Output:", output)

Output:

Output: String and Function



3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
 Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 
Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11 

Program:

def count_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    special_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1
        elif not char.isspace():
            special_count += 1

    return uppercase_count, lowercase_count, number_count, special_count

# Example usage
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, numbers, specials = count_characters(input_string)

print(f"UpperCase : {uppercase}")
print(f"LowerCase : {lowercase}")
print(f"NumberCase : {numbers}")
print(f"SpecialCase : {specials}")


Output:

UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 3

	


4. Write a Python Count vowels in a string 
input= “Welcome to Python Assignment” 
Output: Total vowels are: 8


Program:

string = "Welcome to Python Assignment"

vowels = "aeiouAEIOU"
found_vowels = [char for char in string if char in vowels]

print(f"Vowel Count: {len(found_vowels)}")
print(f"Vowels Found: {(found_vowels)}")


Output:

Vowel Count: 8
Vowels Found: ['e', 'o', 'e', 'o', 'o', 'A', 'i', 'e']