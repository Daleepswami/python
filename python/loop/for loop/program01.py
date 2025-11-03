#take a input a number and find which numbers divide it and how many number can divide it.
num=int(input("Enter a nuber"))
count=0
for i in range(1,num+1):
    if num%i==0:
       count+=1
       print(f"{num} is divide by {i}")
    
