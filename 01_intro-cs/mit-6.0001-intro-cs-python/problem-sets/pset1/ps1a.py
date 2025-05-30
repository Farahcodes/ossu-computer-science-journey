## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0.0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
total_down_payment = cost_of_dream_home * portion_down_payment

while amount_saved < total_down_payment:
    monthly_return = amount_saved * (r / 12)
    monthly_salary_savings = (yearly_salary / 12) * portion_saved
    amount_saved += monthly_return + monthly_salary_savings
    months += 1

print("Number of months:", months)
