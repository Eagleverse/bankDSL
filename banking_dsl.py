
import random
import string


###################################
#####     MAIN :)             #####
###################################

def main():
    print("Hello Bank!")


# END
if __name__ == "__main__":
    main()


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)


class Account:
    def __init__(self, owner):
        self.owner = owner
        self.name = f"{owner.first_name} {owner.last_name}"
        self.account_number = self.generate_account_number(owner.first_name, owner.last_name)
        self.balance = 0.0
        self.transactions = 0

    def generate_account_number(self, first_name, last_name):
        prefix = first_name[0].upper() + last_name[0].upper()
        suffix = ''.join(random.choices(string.digits, k=6))
        return prefix + suffix

    def transact(self, type, amount):
        if type == 'deposit':
            self.balance += amount
        elif type == 'withdrawal':
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Unknown transaction type")
        self.transactions += 1

    def transaction_count(self):
        return self.transactions

    def current_balance(self):
        return self.balance
