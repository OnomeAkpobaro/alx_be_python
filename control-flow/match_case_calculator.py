#Match Case Calculator

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

#Ask the user for the operation 
operation = input("Choose the operation (+, -, *, /): ")


#Match case calculations

match operation:
    
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")