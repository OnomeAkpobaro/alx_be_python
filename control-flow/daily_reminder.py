#Daily Reminder

#Prompt the user for the task description
task = input("Enter your task: ")

#Prompt the user for the task priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

#Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

#Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority. Please use 'high', 'medium', or 'low'."
        print(reminder)
        exit()      #Exit the program if an invalid priority is entered

#Check if the task is time-bound using if statement
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."

else:
    print("Invalid input for time sensitivity. Pleasenuse 'yes' or 'no'.")
    exit()          #Exit the program if an invalid response is entered

    #Print the final customized reminder
print(f"Reminder: {reminder}")
