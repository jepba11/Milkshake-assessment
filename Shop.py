#define constants
DISCOUNT = 0.75 #default sale discount
SPDISCOUNT = 0.9 #special discount for 3+ items or purchases of over $100

#define lists
ItemsForSale = ['Jeans','T-Shirts','Shoes','Socks','Skirts'] #list name says it all

RetailPrice = [55, 30, 45, 5, 25] #retail price for items
#print([f"${price:.2f}" for price in RetailPrice]) #test list logic

PriceAfterSale = [DISCOUNT * price for price in RetailPrice]
#print([f"${price:.2f}" for price in PriceAfterSale]) #test list logic

TotalCustomerSales = [] #stores total sales for the session

#define functions
def welcomeMessage():
    print("\n\n\n\nWelcome to this Factory Outlet! We currently have a sale of 25% off all stocked items!\n"
          "If you purchase 3 or more items, or if your total purchase is over $100,\n"
          "you will receive an additional 10% off your total purchase.") #small intro msg split across multiple lines for readability
    
    input("\n\nPress Enter to continue...") #breaking up the text for user qol

def newCustomer():

    #per-customer lists
    Order = []
    RetailCost = []
    SaleCost = []
    SpecialDiscount = []

    #print welcome message and sale info
    welcomeMessage()

    #print stocked items
    itemSelected = False
    while itemSelected == False:
     print("\nAvailable items:")
     for i in range(len(ItemsForSale)):
         print(f"- {ItemsForSale[i]} -Item code: {i+1} - ${RetailPrice[i]:.2f} - Sale Price: ${PriceAfterSale[i]:.2f}") #lists all stocked items and their retail + discount price
    
     print("\n What would you like to buy today?")
     itemTypes = input("Please enter the item code for the item(s) the customer would like to buy, sperated by a comma.\n"
           "E.g. 1,2,3 for Jeans, T-Shirts, and Shoes: ").split(",") #splits input into a list of item codes, seperated by a comma
     print(itemTypes) #test list logic
     itemTypes = [item.strip() for item in itemTypes] #removes whitespace from each item in the list
     print(itemTypes) #test list logic
     if len(itemTypes) == 0:
         print("No items were selected. Please try again.")
         itemSelected = False
     else:
         itemSelected = True


#welcome msg
print("Hello and welcome to the cash register program.")
input("\nPress Enter to continue...") #the message above isnt even seen if this isnt here
customerAtRegister = True

#main loop
while customerAtRegister == True:

    newCustomer()


    isCustomerAtRegister = input("Is there another customer in the line? Y or N: ").strip().upper()

    if isCustomerAtRegister == "Y":
        customerAtRegister = True
    elif isCustomerAtRegister == "N":
        customerAtRegister = False
    else:
        print("Please enter Y or N.")
