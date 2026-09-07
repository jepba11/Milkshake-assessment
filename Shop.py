#define constants
DISCOUNT = 0.75
SPDISCOUNT = 0.9

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
