import sys

# check if the correct number of command line arguments is provided
if len(sys.argv) !=2:
    print("usage:python even_odd_checker.py<number>")
    sys.exit(1)
    
#get the number from the command line argument
    number=int(sys.argv[1])
    
#check if the number is even or odd
    if number % 2==0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
