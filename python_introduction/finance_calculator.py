# Prompt the user for their monthly income
monthly_income = int(input("Enter your monthly income: "))

# Ask for their total monthly expenses
monthly_expenses = int(input("Enter yout total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

#Assume a simple interest rate of 5%
annual_interest_rate = 0.05

# Calculate the projected savings after one year with interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * annual_interest_rate)

# Output the result
print(f"Your monthly savings are ${monthly_savings:}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:}.")