"""
Purpose: Ration Store

    item    cost        quantity        Amount
    --------------------------------------------
    wheat   25/kg       30kgs   25*30 = 750/-
    Rice    12/kg       50kgs   12*50 = 600/-
                                --------------
                                        1350/-
                            subsidy 20% -270/-
                            -------------------
                            BillableAmount:1080/- 

Algorithm
---------
Step 1 : Get the cost of items into variables
Step 2 : Get the quantity of items into variables
Step 3 : Compute the selling price of each item,
         and add them
Step 4 : Compute the subsidy amount and substract
         from selling price
Step 5 : Display the Billable Amount

"""

# cost of the Items
cost_of_wheat = 25
cost_of_rice = 12

# Quantities of Items
qty_of_wheat = 30   #kgs
qty_of_rice = 50    #kgs

# Selling Price Computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_rice + sp_of_wheat
#print(total_sp)
print("Total selling Price  :", total_sp)

# Subsidy calculation at 20% subsidy
subsidy_amount = (total_sp * 20)/100 #PEMDAS
print("Subsidy amount   :", subsidy_amount)

billable_amount = total_sp - subsidy_amount
print("Billable Amount :", billable_amount)
