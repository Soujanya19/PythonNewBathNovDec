# cost of items
cost_of_rice = 10 #per kg
cost_of_wheat = 34 #per kg

# Quamtities of item
#convert input to float
#input value is taken as string when executed 
#so convert to float
qty_of_rice = float(input("Enter qty of rice (in kgs):"))
print("Qty of Rice :", qty_of_rice)

qty_of_wheat = input("Enter qty of Wheat(in kgs):")
qty_of_wheat = float(qty_of_wheat)
print("Qty of Wheat :", qty_of_wheat)

#Selling prie computation
sp_of_rice = cost_of_rice * qty_of_rice
print("SP of rice :", sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("SP of wheat :", sp_of_wheat)

total_sp = sp_of_rice + sp_of_wheat
print("Total SP     :", total_sp)