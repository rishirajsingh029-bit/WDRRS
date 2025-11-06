import datetime
import os

# Predefined item list with prices
PRODUCTS = {
    "milk": 40,
    "bread": 25,
    "eggs": 6,
    "rice": 70,
    "sugar": 45,
    "oil": 150,
    "soap": 30,
    "salt": 20,
    "chips": 10,
    "juice": 35
}
cart = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_products():
    print("\nAvailable Products:")
    print("-" * 35)
    for name, price in PRODUCTS.items():
        print(f"{name.title():15s} ₹{price}")
    print("-" * 35)

def add_to_cart():
    item = input("\nEnter product name: ").lower()
    if item not in PRODUCTS:
        print("❌ Item not found! Try again.")
        return
    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("❌ Quantity must be positive!")
            return
        cart[item] = cart.get(item, 0) + qty
        print(f"✅ Added {qty} x {item.title()} to cart.")
    except ValueError:
        print("❌ Please enter a valid number.")

def view_cart():
    if not cart:
        print("\n🛒 Cart is empty.")
        return
    print("\n🧾 Your Cart:")
    print("-" * 35)
    total = 0
    for item, qty in cart.items():
        price = PRODUCTS[item]
        cost = price * qty
        total += cost
        print(f"{item.title():15s} x {qty:<3d} = ₹{cost}")
    print("-" * 35)
    print(f"Subtotal: ₹{total}")
    print("-" * 35)

def generate_bill():
    if not cart:
        print("\n⚠️ Cannot generate bill — cart is empty.")
        return False  # Return False to continue to main menu

    total = sum(PRODUCTS[item] * qty for item, qty in cart.items())
    tax = round(total * 0.18, 2)
    final = total + tax

    # Display bill before payment decision
    print("\n🧾 Generating Bill:")
    print("=" * 35)
    print(" VITMart BILL")
    print("=" * 35)
    print(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 35)
    for item, qty in cart.items():
        cost = PRODUCTS[item] * qty
        print(f"{item.title():15s} x {qty:<3d} = ₹{cost}")
    print("-" * 35)
    print(f"Subtotal: ₹{total}")
    print(f"Tax (18%): ₹{tax}")
    print(f"Total: ₹{final}")
    print("=" * 35)

    # Prompt to proceed with payment or return to main menu
    print("\nWhat would you like to do next?")
    print("1. Proceed to Payment")
    print("2. Return to Main Menu")
    while True:
        choice = input("\nEnter your choice (1-2): ")
        if choice == "1":
            print("\n✅ Proceeding to payment...")
            break
        elif choice == "2":
            print("\n✅ Returning to main menu...")
            return False  # Return False to keep cart and continue to main menu
        else:
            print("❌ Invalid choice. Please choose 1 or 2.")

    # Payment options
    print("\nSelect Payment Method:")
    print("1. Cash")
    print("2. Credit Card")
    print("3. UPI")
    print("4. Debit Card")
    while True:
        payment_choice = input("\nEnter payment method (1-4): ")
        payment_methods = {
            "1": "Cash",
            "2": "Credit Card",
            "3": "UPI",
            "4": "Debit Card"
        }
        if payment_choice in payment_methods:
            payment_method = payment_methods[payment_choice]
            print(f"✅ Payment selected: {payment_method}")
            break
        else:
            print("❌ Invalid payment method. Please choose 1-4.")

    # Generate final bill with payment method
    bill = []
    bill.append("=" * 35)
    bill.append(" VITMart BILL")
    bill.append("=" * 35)
    bill.append(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    bill.append("-" * 35)
    for item, qty in cart.items():
        cost = PRODUCTS[item] * qty
        bill.append(f"{item.title():15s} x {qty:<3d} = ₹{cost}")
    bill.append("-" * 35)
    bill.append(f"Subtotal: ₹{total}")
    bill.append(f"Tax (18%): ₹{tax}")
    bill.append(f"Total: ₹{final}")
    bill.append(f"Payment Method: {payment_method}")
    bill.append("=" * 35)
    bill.append("Thank you for shopping at VITMart!")
    bill.append("=" * 35)
    bill_text = "\n".join(bill)

    # Print final bill to screen
    print("\n" + bill_text)

    # Save to file with utf-8 encoding
    if os.path.exists("bill.txt"):
        print("⚠️ 'bill.txt' already exists. Overwriting...")
    with open("bill.txt", "w", encoding='utf-8') as f:
        f.write(bill_text)
    print("\n🧾 Bill saved as 'bill.txt' in current folder.")

    # Clear cart after successful bill generation
    cart.clear()
    print("\n👋 Thank you for shopping at VITMart!")
    return True  # Return True to exit the program after payment

def main():
    while True:
        print("\n====== VITMART BILLING SYSTEM ======")
        print("1. Show Products")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Generate Bill")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            if generate_bill():  # If True, exit the program
                break
        elif choice == "5":
            print("\n👋 Thank you for using VITMart!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    clear_screen()
    main()

