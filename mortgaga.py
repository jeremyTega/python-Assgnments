# Pseudocode:
# Monthly Loan Payment Calculator
#
# collect the principal amount from the user
#
# collect the annual interest rate (in percent) from the user
#
# collect the loan duration in years from the user
#
# Convert the annual interest rate to a monthly rate:
#
# Calculate the total number of monthly payments:
#
# Use the loan amortization formula to calculate monthly payment:
#
# Display the monthly payment, formatted to 2 decimal places




principal = float(input("enter princpal amount"))
interestRate = float(input("enter annual interest rate"))
durunationYears = float(input("enter the durunation in years"))

rate =interestRate/(100*12)
numberOfPayments = durunationYears * 12
#monthlyPayment = (princpal * (rate*(1+rate)**numberOfPayments) / (1+rate)**numberOfPayments-1)
monthlyPayment = (principal * rate * (1 + rate) ** numberOfPayments) / ((1 + rate) ** numberOfPayments - 1)

print("Your monthly payment is: {:.2f}".format(monthlyPayment))






