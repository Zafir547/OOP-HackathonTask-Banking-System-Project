import uuid

class BankAccount:
    def __init__(self, account_holder):
        self.account_number = str(uuid.uuid4())[:8]
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ${amount}")
            print(f"${amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def add_transaction(self, description):
        self.transactions.append(description)    

    def print_statement(self):
        print(f"\nTransaction Statement for {self.account_holder}:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Final Balance ${self.balance}\n")

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def open_account(self, account_holder):
        new_account = BankAccount(account_holder)
        self.accounts[new_account.account_number] = new_account
        print(f"Account created successfully! Account Number: {new_account.account_number}")
        return new_account.account_number
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)

        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred ${amount} from {sender_account_number} to {receiver_account_number}")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("One both accounts not found.")

    def admin_check_total_deposit(self):
        total_depsoit = sum(account.balance for account in self.accounts.values())
        print(f"Total deposits in the bank: ${total_depsoit}")

    def admin_check_total_accounts(self):
        print(f"Total number of accounts: {len(self.accounts)}")

def main():
    bank = Bank()
    while True:
        print("\n*** Banking System Menu ***")
        print("1. Open New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Tranfer Money")
        print("6. Print Statement")
        print("7. Admin: Total Deposits")
        print("8. Admin: Total Accounts")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            bank.open_account(name)
        elif choice == '2':
            acc_number = input("Enter account number: ")
            acc = bank.get_account(acc_number)
            if acc:
                amount = float(input("Enter amount to deposit: $"))
                acc.deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            acc_number = input("Enter account number: ")
            acc = bank.get_account(acc_number)
            if acc:
                amount = float(input("Enter amount to withdraw: $"))
                acc.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            acc_number = input("Enter account number: ")
            acc = bank.get_account(acc_number)
            if acc:
                acc.check_balance()
            else:
                print("Account not found.")
        elif choice == '5':
            sender_acc_number = input("Enter sender's account number: ")
            receiver_acc_number = input("Enter receiver's account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(sender_acc_number, receiver_acc_number, amount)
        elif choice == '6':
            acc_number = input("Enter account number: ")
            acc = bank.get_account(acc_number)
            if acc:
                acc.print_statement()
            else:
                print("Account not found.")
        elif choice == '7':
            bank.admin_check_total_deposit()
        elif choice == '8':
            bank.admin_check_total_accounts()
        elif choice == '9':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    