#
#Vikas Patil
#


#Python Lab Assignment -1


Q.1 print helloworld

Solution:

print("Hello World")

Output:

Hello World



Q.2 describe local variable and global variable code

Solution:

a=1 #Global Variable
b=2
def main():
    c=3 #local variable
    d=4
    print (c)
    print (d)

main()

print(a)
print(b)

Output:

3
4
1
2


Q.3 Write a code that describe Indentation error

Solution:

X=10
def main():
X=30
    print ('X=',X)
main()

Output:

  Cell In[18],   line 3
    X=30
    ^
IndentationError: expected an indented block after function definition on line 2



Q.4 write a code that describe local and global variable with same name


Solution:

X=10
def main():
    X=30
    print ('X=',X)

def globalvar():
    global X
   
    print ('X',X)
main()
globalvar()


Output:

= 30
X 10


Q.5 Write a code for string, int and float input.

Solution:

# Taking a string input
name = input("Enter your name: ")
print(f"Name: {name}")
# Taking an integer input
age = int(input("Enter your age: "))
print(f"Age: {age}")
# Taking a float input
height = float(input("Enter your height in meters: "))
print(f"Height: {height} meters")


Output:

Enter your name:  Vikas
Name: Vikas
Enter your age:  24
Age: 24
Enter your height in meters:  1.68
Height: 1.68 meters
