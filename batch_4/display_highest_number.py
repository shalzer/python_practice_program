#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

#create an empty list that stores infinite inputs until invalid
#    get user input as an integer
#    stores the number entered on the list

# if the user input is invalid:
    #the program goes through the list and check the highest number
    #print invalid input and the highest number entered and stop the loop

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)