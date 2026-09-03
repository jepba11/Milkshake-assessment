print("Hello and welcome to the cash register program.")

AmountOfCustomers = int(input("How many customers are in the line?: "))

while AmountOfCustomers > 3:
    print("Line is missmanaged. Please divert extra customers to other registers.")
    AmountOfCustomers = int(input("How many customers are now in the line?:"))
print("Line is now manageable.")

#print(f"The number of customers in the line is: {AmountOfCustomers}")
Productlist=["Jeans", "T-Shirts", "Shoes", "Socks", "Skirts"]
print(f"Items for sale are: {Productlist}")
print("Jeans are $55 would you like to buy any?")
buyJeans = input("Y or N:")
if buyJeans == "Y":
    numofJeans = int(input("How many Jeans would you like to buy?: "))
else:
    print("No Jeans will be purchased.")
if input("Is that everything? Y or N:") == "Y":
    totalPrice = (numofJeans * 55)
    print(f"your total is...{totalPrice}")
#else: