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
        return
    total = sum(PRODUCTS[item] * qty for item, qty in cart.items())
    tax = round(total * 0.18, 2)
    final = total + tax
    bill = []
    bill.append("=" * 35)
    bill.append(" SMARTMART BILL")
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
    bill.append("=" * 35)
    bill.append("Thank you for shopping at SmartMart!")
    bill.append("=" * 35)
    bill_text = "\n".join(bill)
    # Print to screen
    print("\n" + bill_text)
    # Save to file
    if os.path.exists("bill.txt"):
        print("⚠️ 'bill.txt' already exists. Overwriting...")
    with open("bill.txt", "w") as f:
        f.write(bill_text)
    print("\n🧾 Bill saved as 'bill.txt' in current folder.")
    cart.clear()

def main():
    while True:
        print("\n====== SMARTMART BILLING SYSTEM ======")
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
            generate_bill()
        elif choice == "5":
            print("\n👋 Thank you for using SmartMart!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    clear_screen()
    main()
