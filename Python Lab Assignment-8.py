#
#Vikas Patil	
#Python Lab Assignment-8
#



1. Write a Python program to count the occurrences of each word in a
given sentence

string = “To change the overall look of your document. To change the look
available in the gallery”

Program:

from collections import Counter

# Input string
string = "To change the overall look of your document. To change the look available in the gallery"

# Normalize the string to lowercase and remove punctuation
normalized_string = string.lower().replace('.', '')

# Split the string into words
words = normalized_string.split()

# Count occurrences of each word
word_count = Counter(words)

# Print the word count
for word, count in word_count.items():
    print(f"{word}: {count}")

Output:

to: 2
change: 2
the: 3
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1


2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n"

Program:

# Input string
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove all newline characters
cleaned_str = string.replace("\n", "")

# Print the result
print("Original String:")
print(string)
print("\nCleaned String:")
print((cleaned_str))


Output:

Original String:

Best 
Deeptech 
Python 
Training


Cleaned String:
Best Deeptech Python Training

3.Write a Python program to reverse words in a string
  String = “Deeptech Python Training”

Program:

# Input string
string = "Deeptech Python Training"

# Reverse the words and print the result
print(" ".join(string.split()[::-1]))

Output:

Training Python Deeptech


4.Write a Python program to count and display the vowels of a given text
  String=”Welcome to python Training”

Program:


string = "Welcome to python Training"

vowels = "aeiouAEIOU"
found_vowels = [char for char in string if char in vowels]

print(f"Vowel Count: {len(found_vowels)}")
print(f"Vowels Found: {(found_vowels)}")


Output:

Vowel Count: 8
Vowels Found: ['e', 'o', 'e', 'o', 'o', 'a', 'i', 'i']