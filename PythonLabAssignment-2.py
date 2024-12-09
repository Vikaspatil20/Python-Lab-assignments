#
#Vikas Patil
#



Q.1 Write a program for arithmatic operators

Program:

def ex1():
	a = 10
	b = 3
	print(a+b)
	print(a-b)
	print(a*b)
    
	print(a/b)
	print(b/a)
	print(a//b)
	print(b//a)
    
	print(a%b)
	print(b%a)
	print(a**b)
    
#ex1(); 

Output:

13
7
30
3.3333333333333335
0.3
3
0
1
3
1000



Q.2 Write a program for assignment operators

solution:

def ex2():	
    c = 10
    #c+=1
    print(c)
    c += 3 #c = c + 3
    print(c)
    c -= 2 #c = c - 2
    print(c)
    
ex2();

Output:

10
13
11

Q.3 Write a program for Bitwise operators 

Solution:

def ex7():
    a = 9  # 1001 in binary
    b = 8  # 1000 in binary
    print(bin(9))  # Prints binary representation of 9
    print(bin(8))  # Prints binary representation of 8
    print(a & b, bin(a & b))  # Bitwise AND operation between a and b
    print(a | b, bin(a | b))  # Bitwise OR operation between a and b
    print(a ^ b, bin(a ^ b))  # Bitwise XOR operation between a and b

ex7()


Output:

0b1001
0b1000
8 0b1000
9 0b1001
1 0b1



Q.4 Write a program to calculate greatest of three numbers.


Solution:

def find_greatest_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# Example usage
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

greatest = find_greatest_of_three(a, b, c)
print(f"The greatest number among {a}, {b}, and {c} is {greatest}.")

Output:

Enter the first number:  25
Enter the second number:  96
Enter the third number:  24
The greatest number among 25, 96, and 24 is 96.



Q:5) Calculate the area of a circle.

Solution:

#Program to calculate the area of a circle

import math

radius=float(input('Enter the radius of Circle: '))

area= math.pi*radius**2   #Using math.pi for better precision

print(f"The area of the circle is :{area:.2f} ")


Output:

Enter the radius of Circle: 5
The area of the circle is :78.54 


Q:6)Calculate the area of a triangle.

Solution:

#Program to calculate the area of a triangle

breadth=float(input('Enter the breadth of triangle: '))
height=float(input('Enter the height of triangle: '))

Area= 1/2*breadth*height  
print(f"The area of the triangle is :{Area:.2f} ")

Output:

Enter the breadth of triangle: 6
Enter the height of triangle: 4
The area of the triangle is :12.00 

Q:7)Calculate the area of a rectangle.


Solution:


#Program to calculate the area of a rectangle

lenghth=float(input('Enter the lenghth of rectangle: '))
width=float(input('Enter the width of rectangle: '))

Area= lenghth*width
print(f"The area of the rectangle is :{Area:.2f} ")


Output:

Enter the lenghth of rectangle: 6
Enter the width of rectangle: 7
The area of the rectangle is :42.00 


Q:8)Calculate the area of a square

Solution:

#Program to calculate the area of a square

side=float(input('Enter the side length of square: '))


Area= side **2
print(f"The area of the square is :{Area:.2f} ")



Output:

Enter the side length of square: 7
The area of the square is :49.00 

