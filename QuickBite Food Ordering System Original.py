# Menu and prices
menu = {
    "soup and starters": {
        "Chicken and Mushrooms soup": 3.00,
        "Vegetable soup": 3.00,
        "Lamb soup": 3.10
    },
    "rice dishes": {
        "Beef Fried Rice": 6.00,
        "King Prawn Fried Rice": 7.00,
        "Duck Fried Rice": 6.50
    },
    "chop suey dishes": {
        "Chicken Chop Suey": 6.20,
        "Beef Chop Suey": 6.90,
        "Barbecue Pork Chop Suey": 6.30
    },
    "beef dishes":{
        "Beef with Mushrooms": 6.60,
        "Beef with Fresh Tomatoes": 6.60,
        "Beef with Ginger and Spring Onion": 6.60
    }
}

# Basket to hold customer orders
basket = {}


# Function to display the menu
def displayMenu():
    # Print a title header for the menu
    print("\n--- Menu ---")

    # Iterate through each category in the menu dictionary
    for category, items in menu.items():
        # Print the category name, converting it to title case for better readability
        print(f"\n{category.title()}:")

        # Iterate through each item in the current category
        for item, price in items.items():
            # Print the item name and its price formatted to two decimal places
            print(f"{item} - £{price:.2f}")

        # Order management function
def orderManagement():
    global basket
    while True:
        displayMenu()
        selectedItem = input("\nPlease select an item by entering its name: ")
        # Check if selected item is in the menu
        found = False
        for category in menu.values():
            if selectedItem in category:
                price = category[selectedItem]
                found = True
                break

        if found:
            while True:  # Add a loop to re-prompt for quantity until valid
                try:
                    quantity = int(input("Enter the quantity you would like to order: "))
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")
            # Add item to basket or update quantity if already in basket
            if selectedItem in basket:
                basket[selectedItem] += quantity
            else:
                basket[selectedItem] = quantity
            print(f"Item added to basket: {selectedItem} x{quantity}")

            response = input("Would you like to add another item? (yes/no): ").lower()
            if response == 'no':
                print("\nHere is your BASKET:", basket)
                break
        else:
            print("Sorry, that item is not available on the menu.")

# Total bill amount function
def totalBillAmount():
    print("\nYour bill is being processed...")
    total = 0.0
    for item, quantity in basket.items():
        # Find the price of each item in the menu
        for category in menu.values():
            if item in category:
                price = category[item]
                total += price * quantity
                break
    print("\nItems Ordered:", basket)
    print(f"Total Amount: £{total:.2f}")
    return total

# Payment processing function
def paymentProcessing(total):
    while True:
        print("\nPlease select a payment method: Credit Card or PayPal")
        paymentMethod = input("Payment Method: ").lower()
        if paymentMethod not in ["credit card", "paypal"]:
            print("Invalid payment method. Please choose a valid payment method.")
            continue  #Repeats the payment method prompt

        # Simulate payment processing
        paymentSuccess = input("Confirm payment? (yes/no): ").lower()
        if paymentSuccess == 'yes':
            print("Payment Successful. Order Confirmed!")
            break
        else:
            print("Payment failed. Try again.")

# Main ordering process
print("------------------------------------------------------")
print("|====================================================|")
print("|======== Welcome to QuickBite Ordering System ======|")
print("|====================================================|")
print("------------------------------------------------------")

orderManagement()

# Check if basket is empty
if not basket:
    print("Your basket is empty.")
else:
    total = totalBillAmount()
    print("\nProceeding to payment process...")
    paymentProcessing(total)

print("\nThank you for ordering with QuickBite!")