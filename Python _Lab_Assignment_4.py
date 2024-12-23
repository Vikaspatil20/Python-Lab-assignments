
1.     Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

Solution:

Number=int(input('Enter a Number: '))
if Number%2==0:
 print('Entered number is Even')
else:
 print('Entered number is odd')

Output:

Enter a Number:  6
Entered number is Even


2.      Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

Solution:

Age = int(input("Enter a age of person: "))
if Age>18:
    print("Person is elligible to vote")
else:
    print("Person is not elligible to vote")

Output:

Enter a age of person:  19
Person is elligible to vote 


3.      Write a Python program that determines if a given year is a leap year or not.

Solution:


Year = int(input("Enter a Year: "))
if Year%4==0:
    print("Entered year is leap year")
else:
    print("Entered year is not leap year")


Output:

Enter a Year:  2022
Entered year is not leap year

4.      Create a Python program that checks if a user-given number is positive, negative, or zero.

Solution:

Number = float(input("Enter a Number: "))
if Number==0:
    print("Entered Number is 0")
elif Number<0:
    print("Entered Number is Negative")    
else:
    print("Entered Number is Positive")

Output:

Enter a Number:  5
Entered Number is Positive



5.      Write a Python program that determines the largest of three numbers entered by the user.

Solution:

a = float(input("Enter first Number: "))
b = float(input("Enter second Number: "))
c = float(input("Enter third Number: "))

max_num=a

# Compare with the second number
if b > max_num:
    max_num=b
   
# Compare with the third number
if c > max_num:
    max_num=c

# Print the maximum number
print(f"The largest number is: {max_num}")

Output:

Enter first Number:  05
Enter second Number:  55
Enter third Number:  60
The largest number is: 60.0
