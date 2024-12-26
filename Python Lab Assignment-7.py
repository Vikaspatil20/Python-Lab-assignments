#
#Vikas Patil	
#Lab Assignment-6
#


1.Print the table of 5 using for loop

Solution:

for i in range(1, 11): 
    print(f"5 x {i} = {5 * i}")

Output:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

2.Print even number series by taking input from the user:

Solution:

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Even number series:")
for num in range(start, end + 1): 
    if num % 2 == 0: 
        print(num)

Output:

Enter the starting number:  2
Enter the ending number:  18
Even number series:
2
4
6
8
10
12
14
16
18

3.Create a list and iterate through its items using a for loop:

Solution:

my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Iterate through the list using a for loop
print("Items in the list:")
for item in my_list:
    print(item)

Output:

Items in the list:
apple
banana
cherry
date
elderberry


4.Calculate the sum of numbers from 1 to 10 


Solution:

total_sum = 0

for num in range(1, 11):
    total_sum += num  # Add each number to the sum

print(f"The sum of numbers from 1 to 10 is: {total_sum}")

Output:

The sum of numbers from 1 to 10 is: 55


5.print the pattern   

          *

         ***

       *****

      *******

     *********


Solution:

# Number of rows for the pattern
rows = 5

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))

Output:

    *
   ***
  *****
 *******
*********


6. Print the first 10 natural numbers using for loop 

Solution:

print("The first 10 natural numbers are:")
for i in range(1, 11):  # Loop from 1 to 10
    print(i)

Output:

The first 10 natural numbers are:
1
2
3
4
5
6
7
8
9
10



7. Python program to check if the given string is a palindrome 

Solution:

# Take input from the user
string = input("Enter a string: ")

# Initialize a flag
is_palindrome = True

# Use a for loop to check each character
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:  # Compare characters from the start and the end
        is_palindrome = False
        break

# Output the result
if is_palindrome:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')


Output:

Enter a string:  naman
"naman" is a palindrome.



 8.Python program to get the Fibonacci series between 0 to 50 


Solution:

# Initialize the first two numbers of the Fibonacci series
a, b = 0, 1

print("Fibonacci series between 0 and 50:")
print(a, end=" ")  # Print the first number

# Use a for loop to generate Fibonacci numbers
for _ in range(50):  # Maximum iterations to ensure we cover the range
    if b > 50:  # Stop if the next number exceeds 50
        break
    print(b, end=" ")  # Print the next number
    a, b = b, a + b  # Update to the next numbers in the series


Output:

Fibonacci series between 0 and 50:
0 1 1 2 3 5 8 13 21 34

