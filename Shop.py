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
          "you will receive an additional 10% off your total purchase."
          "\n\nPlease note that during this sale we have a limit of 10 items per type of item per customer. "
          "\nThank you for your understanding") #small intro msg split across multiple lines for readability
    
    input("\nPress Enter to continue...") #breaking up the text for user qol

def addToOrder(selectedItems):
    order = []

    for itemCode in selectedItems:
        try:
            itemCode = int(itemCode)
        except ValueError:
            print(f"Invalid item code '{itemCode}'. Skipping this item.")
            continue

        if itemCode < 1 or itemCode > len(ItemsForSale):
            print(f"Item code {itemCode} is not valid. Please choose a valid code.")
            continue

        while True:
            try:
                quantity = int(input(f"How many {ItemsForSale[itemCode - 1]} would you like? ").strip())
            except ValueError:
                print("Please enter a valid whole number.")
                continue

            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue

            if quantity > 10:
                print(f"You can only buy up to 10 of each item per customer. Please choose a quantity between 0 and 10.")
                continue

            break

        for _ in range(quantity):
            order.append(itemCode)

    return order


def calculateCustomerSubtotal(order):
    subtotal = 0
    for itemCode in order:
        subtotal += PriceAfterSale[itemCode - 1]
    return subtotal

def applySpecialDiscount(subtotal, order):
    if len(order) >= 3 or subtotal > 100:
        return subtotal * SPDISCOUNT
    return subtotal

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
     itemTypes = input("Please enter the item code for the item(s) the customer would like to buy, sperated by a comma. \n"
                       "ENSURE THAT IT IS A VALID ITEM CODE FROM THE LIST ABOVE\n"
                        "E.g. 1,2,3 for Jeans, T-Shirts, and Shoes: ").split(",") #splits input into a list of item codes, seperated by a comma

     itemTypes = [item.strip() for item in itemTypes if item.strip() != ""] #removes whitespace from each item in the list

     if len(itemTypes) == 0:
         print("No items were selected. Please try again.")
         itemSelected = False
         continue

     validItemCodes = []
     invalidItemCodes = []

     for item in itemTypes:
         try:
             code = int(item)
         except ValueError:
             invalidItemCodes.append(item)
             continue

         if 1 <= code <= len(ItemsForSale):
             validItemCodes.append(code)
         else:
             invalidItemCodes.append(item)

     if len(validItemCodes) == 0:
         print("No valid item codes were selected. Please try again.")
         itemSelected = False
         continue

     if len(invalidItemCodes) > 0:
         print(f"The following item codes are invalid and will be ignored: {invalidItemCodes}")

     Order = addToOrder(validItemCodes)
     RetailCost = [RetailPrice[itemCode - 1] for itemCode in Order]
     SaleCost = [PriceAfterSale[itemCode - 1] for itemCode in Order]
     SpecialDiscount = [SPDISCOUNT for _ in Order]
     itemSelected = True

    print("\nCustomer order:")
    itemCounts = {}
    for itemCode in Order:
        itemName = ItemsForSale[itemCode - 1]
        itemCounts[itemName] = itemCounts.get(itemName, 0) + 1

    for itemName, count in itemCounts.items():
        print(f"- {count}x {itemName}")

    subtotal = calculateCustomerSubtotal(Order)
    print(f"\nSubtotal: ${subtotal:.2f}")

    total = applySpecialDiscount(subtotal, Order)
    if total < subtotal:
        print(f"Special discount applied! New total: ${total:.2f}")
    else:
        print(f"Total: ${total:.2f}")


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
