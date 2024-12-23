#
#Vikas Patil
#Python Lab Assignment-6
#






1.) Print the reverse order series  using a while loop

Solution:

a=10
b=0
while a>=b:
    print(a,end=' ')
    a-=1

Output:

10 9 8 7 6 5 4 3 2 1 0 



2.) Create a code that describe the use of break statement in while loop

Solution:

a = 1
while a < 7:
    print(a)
    if a == 4:
        break
    a += 1  

Output:

1
2
3
4




3.) Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

Solution:

string = "Python"
i= 0

while i < len(string):
    print(string[i])  
    i += 1  

length_of_string = len(string)
print("Length of the string:", length_of_string)

Output:

P
y
t
h
o
n
Length of the string: 6


4.) Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.


Solution:

num = int(input("Enter a number to calculate its factorial: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of {num} is {factorial}.")

Output:

Enter a number to calculate its factorial:  5
The factorial of 5 is 120.



5.) Write a python program to check whether a number is palindrome or not? 


Solution:

num = int(input("Enter a number: "))
original_num = num
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

if original_num == reverse_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")


Output:

Enter a number:  454
454 is a palindrome.


6.) Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

Solution:


total_sum = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total_sum += num

print(f"The sum of all entered numbers is {total_sum}.")



Output:

Enter a number (enter 0 to stop):  5
Enter a number (enter 0 to stop):  6
Enter a number (enter 0 to stop):  0
The sum of all entered numbers is 11.