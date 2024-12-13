#
#Vikas Patil
#


1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 

Solution:

# Define the function
def div(a, b):
    # Check if the divisor is not zero
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# Call the function with two numbers and display the result
result = div(10, 2)  # Replace 10 and 2 with your numbers
print("The division result is:", result)

Output:

The division result is: 5.0


2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number . 

Solution:

def square(a):
    b=a*a
    print (f'Square is : {b}')
square(6)    


Output:

Square is : 36


3. Using max() and min() functions display the maximum and minimum of 5 random numbers. 

Solution:

import random
numbers=[random.randint(1,100) for _ in range(5)]
print(f'Random Numbers are: {numbers}')
max_number=max(numbers)
min_number=min(numbers)

print(f'Maximum Number is: {max_number}')
print(f'Minimum Number is: {min_number}')

Output:

Random Numbers are: [61, 3, 31, 48, 79]
Maximum Number is: 79
Minimum Number is: 3


4. Accept a name from the user and display that in lower case using lower() function

Solution:

def display_lowercase():
    name = input('Enter the name: ')
    print('Name in lowercase is:', name.lower())

# Call the function
display_lowercase()

Output:

Enter the name:  SAI
Name in lowercase is: sai