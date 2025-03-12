#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

#initialize num to 0
#loop while num less than or equal to 0
#  check if num does not end in 0
#    if true, print the number
#  increase num by 1

num = 0
while num <= 100:
        if num % 10 != 0:
                print(num)
        num+=1