class ATM:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return f'Current Balance: ₹{self.balance}'

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal of ₹{amount}')
            return f'₹{amount} withdrawn successfully.'
        else:
            return 'Invalid withdrawal amount.'

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit of ₹{amount}')
            return f'₹{amount} deposited successfully.'
        else:
            return 'Invalid deposit amount.'

    def change_pin(self, new_pin):
        self.pin = new_pin
        return 'PIN changed successfully.'

    def get_transaction_history(self):
        return self.transaction_history


account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")

my_atm = ATM(account_number, pin)

while True:
    print("\n1. Check Balance\n2. Withdraw Cash\n3. Deposit Cash\n4. Change PIN\n5. Transaction History\n6. Exit")
    choice = input("\nEnter your choice: ")

    if choice == '1':
        print(f"\n{my_atm.check_balance()}")

    elif choice == '2':
        amount = float(input("\nEnter the amount to withdraw: "))
        print(my_atm.withdraw(amount))

    elif choice == '3':
        amount = float(input("\nEnter the amount to deposit: "))
        print(my_atm.deposit(amount))

    elif choice == '4':
        new_pin = input("\nEnter your new PIN: ")
        print(my_atm.change_pin(new_pin))

    elif choice == '5':
        print("\nTransaction History:")
        for transaction in my_atm.get_transaction_history():
            print(transaction)

    elif choice == '6':
        print("\nThank you for using the ATM. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")