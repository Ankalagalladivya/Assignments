# Input three numbers
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
num3 = float(input("enter the third number:"))

#using conditional statements to find the ascending order
if num1<=num2 and num1<=num3:
    if num2<=num3:
        print("Ascending order:",num1, num2, num3)
    else:
        print("Ascending order:",num1, num3, num2)
elif num2<=num1 and num2<=num3:
    if num1<=num3:
        print("Ascending order:",num2, num1, num3)
        else:
            print("Ascending order:",num2, num3, num1)
else:
    if num1<=num2:
        print("Ascending order:",num3, num1, num2)
    else:
        print("Ascending order:",num3, num2, num1)
        
        
        
        
        
    

