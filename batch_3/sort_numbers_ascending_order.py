#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

#create an empty list that stores infinite numbers entered

#start an infinite loop that ask for user input
#    try to get user input as an integer

# if the user input is invalid:
    #print invalid input and the ascending order of number entered and stop the loop

numbers = []

while True:
    try:
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)
        numbers.sort()
    except ValueError:
        print("invalid input. The ascending order of what you entered is: ", numbers)
        break