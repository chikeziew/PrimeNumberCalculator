# Program to check whether a number is prime, and further whether it can be written in the form x^2 + 1
# Created by: Chikezie Wood, Nov. 14, 2022.

# This program has two main parts - it will identify whether the user inputted number is prime
# If prime, then it will check if the number can be written in the form x^2 + 1

# P R I M E   N U M B E R   C H E C K E R 

# Take input from user
num = 1
while num != "0":
    num = int(input("Enter a number (or ""0"" to exit): "))
    if num == 0:
        quit()

# Define a flag variable
    flag = False 

# Prime Algorithm
    if num > 1:
        # check for factors
        for i in range (2, num):
            if (num % i) == 0:
                #if factor is found, set flag to True
                flag = True 
                break
            else: flag = False

    # check if flag is True
    if flag == True:
        print (num,"is not a prime number")   
    else:
        print (num,"is a prime number.")


    # F O R M  (x^2 + 1)  C H E C K E R

    form_flag = False

    if flag == False:
        y = int(num - 1)
        z = int(y/2) 
        for i in range (2, z):
            if (i*i) == y:
                form_flag = True
                break

        if form_flag == True:
            print (num, "can be written in the form ", i,"x",i,"+ 1.")
        else:
            print (num,"can not be written in the form x^2 + 1.")
