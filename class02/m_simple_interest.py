"""
Purpose : Bank Loan         

Input : P = 10000
        R = 5
        T = 5

Output :2500.0

We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 
units of time.

"""
print("Enter the Principal amount:")

# take input Principal value from user
principal_amt = int(input("Principal:"))

rate_of_interest = int(input("Rate of interest:"))
time = int(input("Time:"))

simple_interest = (principal_amt * rate_of_interest * time)/100

print("Simple Interest is: ", simple_interest)
