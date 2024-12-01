
def authenticate(users):
    pin = input("Enter your 4-digit PIN: ")
    if pin in users:
        print(f"Welcome, {users[pin]['name']}!")
        return pin
    else:
        print("Invalid PIN. Try again.")
        return None

def show_menu():
    print("\nATM Menu:")
    print("1. Balance Inquiry")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance(users, pin):
    print(f"Your current balance is: ₹{users[pin]['balance']}")

def deposit(users, pin):
    amount = float(input("Enter the amount to deposit: "))
    users[pin]['balance'] += amount
    print(f"₹{amount} deposited successfully.")

def withdraw(users, pin):
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= users[pin]['balance']:
        users[pin]['balance'] -= amount
        print(f"₹{amount} withdrawn successfully.")
    else:
        print("Insufficient balance.")

def atm_simulation():
    users = {
        "1234": {"balance": 5000, "name": "John Doe"},
        "5678": {"balance": 3000, "name": "Jane Smith"}
    }
    print("Welcome to the ATM!")
    pin = None
    while not pin:
        pin = authenticate(users)
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            check_balance(users, pin)
        elif choice == "2":
            deposit(users, pin)
        elif choice == "3":
            withdraw(users, pin)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


atm_simulation()
