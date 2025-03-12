#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# ask user to input num1 and num2
# check if num1 is smaller than num2
# print num1 if it's smaller
# print num2 if not

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 < num2:
    print(num1)

else:
    print(num2)