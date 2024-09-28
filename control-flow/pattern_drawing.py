#Pattern Drawing 


#Prompt the user to enter the size of the pattern 
size = int(input("Enter the size of the pattern: "))

#Initialize the row counter
row = 0

#Use while loop to iterate through each row
while row < size:
    #Use a for loop to print asterisks for each column in the row
    for col in range(size):
        print("*", end="")

    #Move to the next line after each row
    print()

    #Increase the row counter
    row = 1