# coding: utf-8
import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]

# len() provides the count of the items in the list.
loan_number = len(loan_costs)
print(f"There are {loan_number} loans.")

# sum() provides the sum of the amounts in the list.
loan_sum = sum(loan_costs)
print(f"The total value of the loans is ${loan_sum:,.2f}.")

# calculates the average loan by dividing the sum by the number of items in the list.
loan_average = loan_sum/loan_number
print(f"The average value of the loans is ${loan_average:,.2f}.")

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# use the .get() construction to pull a value from the dictionary using the string key.
 
remaining_months = loan.get("remaining_months")
future_value = loan.get("future_value")

print(remaining_months, future_value)

# given the discount rate, use the retreived variables to calculate the present value of the loan.
discount_rate = 0.20

loan_present_value = future_value / (1+discount_rate/12) ** remaining_months

print(f"The present value of the loan is ${loan_present_value:,.2f}")

# return to the dictionary to pull the loan price from the dictionary using .get command.
loan_price = loan.get("loan_price")

# compare the loan present value to the loan price and display an evaluation.
if loan_present_value > loan_price:
    print(f"This loan is worth ${loan_present_value:,.2f}, but costs only ${loan_price:,.2f}.  So, the loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price")

# given loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# create the present value function
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value_formula = future_value / (1+annual_discount_rate/12) ** remaining_months
    return present_value_formula

# call the present value function using data from the new loan dictionary
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], 0.20)

print(f"The present value of the loan is: ${present_value:,.2f}")

# loan list of loan dictionaries
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# empty list to hold inexpensive loan data
inexpensive_loans=[]

# for loop to pull loans and append loans below $500
for loan in loans:
    loan_price = loan.get("loan_price")

    if loan_price <= 500:
        inexpensive_loans.append(loan)

print(inexpensive_loans)

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# outputs to same directory and provides file name in csv format.
output_path = Path("inexpensive_loans.csv")

# opens output to write, writes the header followed by the remaining rows
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())