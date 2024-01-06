class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
            return True
        else:
            print("Insufficient balance or invalid withdrawal amount.")
            return False


def display_menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")


class ATM:
    def __init__(self, account):
        self.user_account = account

    def run(self):
        choice = 0

        while choice != 4:
            display_menu()
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit_funds()
            elif choice == 3:
                self.withdraw_funds()
            elif choice == 4:
                print("Thank you for using the ATM!")
            else:
                print("Invalid choice. Please enter a valid option.")

    def check_balance(self):
        balance = self.user_account.get_balance()
        print(f"Your account balance: ${balance:.2f}")

    def deposit_funds(self):
        amount = float(input("Enter the deposit amount: $"))
        self.user_account.deposit(amount)

    def withdraw_funds(self):
        amount = float(input("Enter the withdrawal amount: $"))
        self.user_account.withdraw(amount)


if __name__ == "__main__":
    user_account = BankAccount(0)
    atm = ATM(user_account)
    atm.run()