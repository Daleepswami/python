#2. Write a Python program that prompts the user to enter a integer number and then  check the number is leap year or not. 
year= int(input("Enter the integer number "))
if (year%400==0 or (year%4==0 and year%100!=0)):
    print("this a leap year ")
else:
    print("this is not a leap year")
