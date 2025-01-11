"""
Purpose: Fruit

    Items   Price       qty                         Amount
    -----------------------------------------------------
    Apples  12/piece    5 dozens = 5*12=60          12*60
    Mangos  34/piece    3 dozens = 3*12=36          34*36  
                                                -------------
                                                    1944    /-
                                discount   -2%       -38.88/-
                                                --------------
                                                    1905.12/-
                                    GST   +12.5%    +238.14/-
                                                --------------
                                                    2143.26/-


Algorithm:
----------

Step 0 :    declare constants
Step 1 :    Get the cost of the fruits into variables
Step 2 :    Get the quantity of fruits in to variables
            Compute the end quantity by substituting dozen value
Step 3 :    Compute the selling price to each item,
            and add them
Step 4 :    Compute the discount amount and subtract
            from the selling price, to create the payable amount
Step 5 :    Calculate GST amount and add to the payable amount
            to create billable amount
"""

#Constants
DOZEN = 12
DISCOUNT = 2
GST = 12.5/100

#cost of fruits
cost_of_apple = 12  # per piece
cost_of_mango = 34  # per piece

#quantity of fruits
qty_of_apple = 5 * DOZEN    # pieces
qty_of_mango = 3 * DOZEN    # pieces

#Selling price Computation
total_sp = cost_of_apple * qty_of_apple + cost_of_mango * qty_of_mango
print("Total selling price :", total_sp)

#Discount amount computation
discount_amount = (total_sp * DISCOUNT)/100
print("Discount amount is :", discount_amount)

#Payable amount
payable_amount = total_sp - discount_amount
print("Payable amount is :", payable_amount)

#GST
gst_amount = payable_amount * GST
print("GST amount is :", gst_amount)

#Billable amount
billable_amount = payable_amount + gst_amount
print("Billable amount is :", billable_amount)

# round(num, no_of_digits)
print("Billable amount is :", round(billable_amount,2))