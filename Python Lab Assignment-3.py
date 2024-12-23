#
#Vikas Patil
#Python Lab Assignment-3
#




1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

Solution:

a=int(input('Enter the no: '))
if a%2==0:
        print ("Entered no is even")

else:
        print("Entered no is odd")

Output:

Enter the no:  5
Entered no is odd

2. Using input function take two number and then swap the number 

Solution:

a=int(input('Enter the first no: '))
b=int(input('Enter the Second no: '))
a,b=b,a
print(f"After swapping  First number = {a}, Second number = {b}")


Output:

Enter the first no:  6
Enter the Second no:  5
After swapping  First number = 5, Second number = 6




3. Write a Program to Convert Kilometers to Miles 

Solution:

Distance=float(input("Enter distance in km: "))
if Distance>0:
    c= Distance*0.621371
    print (f"Distance in miles is : {c}")


Output:

Enter distance in km:  6
Distance in miles is : 3.7282260000000003


4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

Solution:

P = 200  
R = 5    	
T = 5    

Interest = (P * R * T) / 100
print(f"Interest is: Rs. {Interest}")

Output:

Interest is: Rs. 50.0


