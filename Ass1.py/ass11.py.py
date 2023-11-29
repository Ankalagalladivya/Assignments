#Input three numbers
num1=float(input("enterthe first number:"))
num2=float(input("enterthe second number:"))
num3=float(input("enterthe third number:"))

#compare the numbers to find the greatest
if num1>=num2 and num1>=num3:
    greatest=num1
elif num2>=num1 and num2>=num3:
    greatest=num2
else:
    greatest=num3
#print the greatest number
print("The greatest number is :",greatest)