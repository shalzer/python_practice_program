#Program 2: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Ask the user to input the 1st number
# Ask the user to input the 2nd number
# Check if both numbers are not the same
# Print "Not Equal" if true
# Print "Number 1 and 2 are equal" if false

num1 = float(input("Please enter the 1st number: "))
num2 = float(input("Please enter the 2nd number: "))

if num1 != num2:
    print("Not equal")
else:
    print("Number 1 and 2 are equal")