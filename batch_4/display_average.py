#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

#create an empty list that stores infinite numbers entered

#start an infinite loop that ask for user input
#    get user input as an integer
#    stores input sa list
#    calculates the total by getting the sum of all numbers
#    calculates the average by dividing total and the amount of entered numbers

# if the user input is invalid:
    #print invalid input and the average of numbers (w/ 2 decimals only) and stops the loop.

numbers = []
while True:
    try:
        num = int(input(f"Enter a number: "))
        numbers.append(num)