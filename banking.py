import random
from apparatus.lexer import Lexer
###################################
#####     MAIN :)             #####
###################################

EST = print

#######################################
# RUN
#######################################


# Generate AST
# parser_ = Parser(tokens)
#   ast = parser_.parse()
#  if ast.error: return None, ast.error


class BankAccount:
    def __init__(self, firstname, lastname, initialbal):
        self.firstName = firstname
        self.lastName = lastname
        self.balance = initialbal
        self.id = Octogram()

    def get_name(self):
        return f"{self.lastName}, {self.firstName}"

    def get_account_number(self):
        return self.id

    def get_balance(self):
        return str(self.balance)

    def deposit(self, deposit_):
        self.balance += deposit_

    def withdraw(self, withdraw_):
        # Hypothetical withdrawal.
        hyposbalance = self.balance
        hyposbalance2 = hyposbalance - withdraw_
        if hyposbalance2 >= 0:
            self.balance -= withdraw_
        else:
            print(f"Overdraw error. Cannot take {withdraw_} from {self.balance}.")


def Octogram():
    rand_list = ""
    for i in range(0, 7):
        n = random.randint(0, 9)
        rand_list += str(n)
    return rand_list


class BankSys:
    def __init__(self):
        self.accounts = [
            BankAccount("Chris", "Ennis", 1000),
            BankAccount("James", "Vo", 2500),
            BankAccount("Keagan", "Haar", 750),
            BankAccount("Clark", "Kent", 950),
            BankAccount("Bruce", "Wayne", 7500000),
        ]

    def account_dump(self):
        return self.accounts

    def get_account_by_id(self, account_id):
        for i in self.accounts:
            if i.get_account_number() == account_id:
                return i

    def create_account(self, first_name, last_name, balance):
        self.accounts.append(BankAccount(first_name, last_name, balance))
        print("Account created!")


def main():
    print("Accounts:")
    bank = BankSys()
    for account in bank.account_dump():
        print(f"{account.get_name()}-{account.get_account_number()}")

    if input("Create new account? (yes/no): ").lower() == "yes":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        balance = float(input("Initial deposit: "))
        bank.create_account(first_name, last_name, balance)
        print("Accounts:")
        for account in bank.account_dump():
            print(f"{account.get_name()}-{account.get_account_number()}")

    selected_account = None
    while not selected_account:
        account_id = input("Enter account ID: ")
        selected_account = bank.get_account_by_id(account_id)
        if not selected_account:
            print("Invalid ID. Try again.")

    running = True
    while running:
        print(
            "Selected: "
            + selected_account.get_name()
            + " - "
            + str(selected_account.get_account_number())
        )
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Different account")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            amount = float(input("Deposit: "))
            selected_account.deposit(amount)
        elif choice == "2":
            amount = float(input("Withdraw: "))
            selected_account.withdraw(amount)
        elif choice == "3":
            print(f"Balance: ${selected_account.get_balance()}")
        elif choice == "4":
            selected_account = None
            for account in bank.account_dump():
                print(f"{account.get_name()}-{account.get_account_number()}")
            while not selected_account:
                account_id = input("Enter account ID: ")
                selected_account = bank.get_account_by_id(account_id)
                if not selected_account:
                    print("Invalid ID. Try again.")
        elif choice == "5" or choice.lower() == "exit":
            running = False
        else:
            print("Invalid choice. Try again.")


print("Thank you for using VEH Bank")


def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error


if __name__ == "__main__":
    main()
