"""
Purpose: Feet to Centimeter conversion
    
    1 foot = 12 inches
    1 inch = 2.54 centimeters

Algorithm:

    Step 1 :    Get feet values in runtime
    Step 2 :    Compute from feet to centimeters
                feet to inches, then
                inches to centimeters conversion
    Step 3 :    Display results
    
"""
# constants
FOOT = 12 #inches
INCH = 2.54 # centimeters

# take input from the user
print("Enter your height in feet:")

ht_feet = int(input("Feet: "))
ht_inch = int(input("Inches: "))

# convert feet to inches
ft_in_inches = ht_feet * FOOT

# convert total height from feet to inches 
total_ht_inches = ht_inch + ft_in_inches

# convert height from inches to centimeter
ht_in_cms = total_ht_inches * INCH

print("Height in centimeter is :", ht_in_cms)