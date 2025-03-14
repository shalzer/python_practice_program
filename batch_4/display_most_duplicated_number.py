#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Create an empty list to store infinite numbers
# Start an infinite loop
#    get user input in integer
#    add it to the list (numbers)
# create variable that checks the frequency of all the entered numbers
# if the user input is invalid, the program will terminate and will print the most frequent number that appeared"

numbers = []
while True:
    try:
        num = int(input("Enter a number (or any non-numeric character to stop): "))
        numbers.append(num)
        if numbers:
            most_frequent = max(numbers, key=numbers.count)
    except ValueError:
        print(f"Invalid input. Most repeated number: {most_frequent}")
        break