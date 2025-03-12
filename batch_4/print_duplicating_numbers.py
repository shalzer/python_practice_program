#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#create an empty list
#create a loop that ask user to enter a number 10x
#the entered numbers r stored in the list (numbers)

#create another list for repeating numbers
#  checks if numbers stored in both list does repeat through looping
#  if it repeats:
#     add it to the 2nd list (duplicate_num)

#prints out the duplicate number

number = []

for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    number.append(num)

duplicate_num = []
for num in number:
    if number.count(num) > 1:
        duplicate_num.append(num)

print("Repeated numbers: ", duplicate_num)