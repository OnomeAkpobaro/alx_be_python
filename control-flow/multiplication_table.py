#Multiplication Table

#Prompt the user to enter a number 

number = int(input("Enter a number to see its multiplication table:"))

#Generate the multiplication table
for y in range(1, 11):
    result = number * y
    print(f"{number} * {y}= {result}")