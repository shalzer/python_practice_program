
#crate a list that stores non repeating numbers
#create another list for reiterating numbers
#Loop 10x to get user's input
# if the number has not been entered before:
#   add it to non-repeating list
#   mark the number as seen by adding it to the repeating number list

#print the list of number that without duplicating any

numbers = []
repeating_numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))

    if num not in repeating_numbers:
        numbers.append(num)
        repeating_numbers.append(num)

print("Numbers entered without duplicates:", numbers)