#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

#initialize diff to 0
#make the first number a variable, ask the user to enter a number
#loop 9 numbers to enter remaining 9 numbers:
#   Ask user to enter a number
#   add number to diff variable
#subtract diff from num1
#print result

diff = 0
num1 = int(input("Enter number 1: "))

for i in range(9):
    number = int(input(f"Enter number {i+2}: "))
    diff += number

print(num1 - diff)