#define constants
DISCOUNT = 0.75 #default sale discount
SPDISCOUNT = 0.9 #special discount for 3+ items or purchases of over $100

#define lists
ItemsForSale = ["Jeans","T-Shirts","Shoes","Socks","Skirts"]
SalePrice = []

#define functions

#welcome msg
print("Hello and welcome to the cash register program.")
customerAtRegister = True
#main loop
while customerAtRegister == True:
 
 isCustomerAtRegister = input("Is there another customer in the line? Y or N: ")

 if isCustomerAtRegister == "Y":
     customerAtRegister = True
 elif isCustomerAtRegister == "N":
     customerAtRegister = False
