#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# ask for the first number from user (num1)
# ask for second number from user (num2)
# identify the smaller and larger number
# Loop from the smaller number + 1 to the larger number - 1
#   Print each number in the range

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(min(num1, num2) + 1, max(num1, num2)):
    print(i)