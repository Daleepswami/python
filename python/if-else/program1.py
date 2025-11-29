#1. Write a Python program that prompts the user to enter two numbers and an operator (+, -, *, /).
#   The program should then perform the corresponding operation on the two  numbers and print the result.

num1=float(input("Enter the first number:-"))
num2=float(input("Enter the second number:-"))
opertor=input("Enter the opertor:-")
if opertor=="+":
    result=num1+num2
    print( "addition of two number", result)
elif opertor=="-":
    result=num1-num2
    print("subtraction of two number",result)
elif opertor=="*":
    result=num1*num2
    print("multiple of two number", result)
elif opertor=="//":
    result=num1//num2
    print("Floor Division",result)
elif opertor=="%":
    result=num1%num2
    print("module ",result)
elif opertor=="/":
    result=num1/num2
    print("division",result)
elif opertor=="**":
    result=num1**num2
    print("Exponentiation",result)
else:
    print("please enter the valid opertor")
