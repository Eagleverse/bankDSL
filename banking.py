import random
import string
from apparatus.lexer import Lexer


###################################
#####     MAIN :)             #####
###################################


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

    def transact(self, type_, amount):
        if type_ == 'deposit':
            self.balance += amount
        elif type_ == 'withdrawal':
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


#######################################
# RUN
#######################################


# Generate AST
# parser_ = Parser(tokens)
#   ast = parser_.parse()
#  if ast.error: return None, ast.error

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error


def main():
    text = ""
    while text.strip() != "exit()":
        text = input('BankS > ')
        if text.strip() == "":
            continue
        if text.strip() == "exit()":
            break

        result, error = run('<stdin>', text)
        if error:
            print(error.as_string())
        else:
            print(result)
#
#       if error:
#          print(error.as_string())
#     elif result:
#        if len(result.elements) == 1:
#           print(repr(result.elements[0]))
#      else:
#         print(repr(result))


if __name__ == "__main__":
    main()
