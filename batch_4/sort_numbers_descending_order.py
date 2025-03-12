#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function


#create an empty list that stores infinite numbers entered

#start an infinite loop that ask for user input
#    get user input as an integer

# if the user input is invalid:
    #goes through the list to sort the numbers entered in descending order
    #print invalid input and the descending order of number entered and stop the loop

numbers = []

while True:
    try:
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)
        numbers.sort(reverse=True)