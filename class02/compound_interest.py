"""
Purpose: Compound Interest    A = P*(1+R/100)**T

Principal = 10000
R = 2
T = 1

"""

principal = int(input("Enter principal amount:"))
rate = int(input("Enter rate of interest:"))
time = int(input("Enter time:"))

amount = (principal * (1+rate/100)**time)

compound_interest = amount - principal

print("The Compound Interest is :", compound_interest)