

# Example: Read two integers from the keyboard in a single line with conditionals

# Read the input line
input_line = input("Enter two integers separated by space: ")

# Split the input line into separate values
values = input_line.split()

# Check if there are exactly two values
if len(values) == 2:
    # Parse the values as integers
    try:
        num1 = int(values[0])
        num2 = int(values[1])
        print("You entered:", num1, num2)
    except ValueError:
        print("Please enter valid integers.")
else:
    print("Please enter exactly two values separated by a space.")
