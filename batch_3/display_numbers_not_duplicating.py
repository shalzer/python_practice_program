#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#create an empty list
#create a loop that ask user to enter a number 10x
#the entered numbers r stored in the list (numbers)

#create another list for not repeating numbers
#  checks if numbers stored in both list does not repeat through looping
#  if it does not repeat:
#     add it to the 2nd list (unique_num)

#prints out the number

number = []

for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    number.append(num)
