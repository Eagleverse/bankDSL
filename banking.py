"""
CSC330 Language Design and Implementation
James Vo, Chris Ennis, Keagan Haar
6/23/24
- - -
We certify that the code below is our own work
"""

###################################
#####        CONSTANTS        #####
###################################

DIGITS = '0123456789'  # digit
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # ANY cap or lower -> tokens
MARK = print


###################################
#####         POSITION        #####
###################################
# Initialization of position, reading user inputs
class Position:
    def __init__(self, idx, ln, col):
        self.idx = idx
        self.ln = ln
        self.col = col

    # Advance method position
    def advance(self, current_char=None):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self


###################################
#####         TOKENS          #####
###################################
# Create Tokens (Token Type)
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_ID = 'ID'
TT_KEYWORD = 'KEYWORD'
TT_EQ = 'EQ'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_EOF = 'EOF'

# Define Keywords
KEYWORDS = [
    'def', 'MARK', 'IF', 'ELSE', 'ENDIF', 'WHILE', 'ENDWHILE', 'DEPOSIT', 'WITHDRAWAL'
]


###################################
#####         LEXER           #####
###################################

# Initialize Tokens
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    # Token's based off of this.
    def getType(self):
        return self.type

    def getVal(self):
        return self.value


# Initialize Lexer
class Lexer:
    def __init__(self, text):
        print("Running Lexer")
        self.text = text
        self.pos = Position(0, 0, 0)
        self.current_char = self.text[self.pos.idx]

    # Define advance, a method we use to move on to the next character
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    # Generate our tokens in regard to what characters represent them
    def generate_tokens(self):
        tokens = []

        while self.current_char is not None:
            # Ignore tab and space
            if self.current_char in ' \t':
                self.advance()
            # Identify DIGITS constant
            elif self.current_char in DIGITS:
                tokens.append(self.generate_number())
            # Identify LETTERS constant
            elif self.current_char in LETTERS:
                print("Letter")
                tokens.append(self.generate_identifier())
            # equals
            elif self.current_char == '=':
                tokens.append(Token(TT_EQ, self.current_char))
                self.advance()
            # plus
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, self.current_char))
                self.advance()
            # minus
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, self.current_char))
                self.advance()
            # Else, advance
            else:
                self.advance()
        # End of File, return tokens
        tokens.append(Token(TT_EOF, None))
        return tokens

    # Generate numbers, finding int if dot_count is 0 and float if dot_count is 1
    def generate_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and (self.current_char in DIGITS or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
            num_str += self.current_char
            self.advance()
        # Return tokens
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

    # Generate identifiers which are either matching a keyword or an ID
    def generate_identifier(self):
        id_str = ''
        while self.current_char is not None and (self.current_char in LETTERS or self.current_char in DIGITS):
            id_str += self.current_char
            self.advance()
        tok_type = TT_KEYWORD if id_str in KEYWORDS else TT_ID
        return Token(tok_type, id_str)


###################################
#####         PARSER          #####
###################################

class ParseResult:
    def __init__(self):
        self.node = None
        self.error = None

    def register(self, res):
        if res.error:
            self.error = res.error
        return res

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self


class MockNode:
    def __init__(self, value):
        self.kind = value


class IntNode:
    def __init__(self, value):
        self.kind = value


class FloatNode:
    def __init__(self, value):
        self.kind = value


class KWNode:
    def __init__(self, value):
        self.kind = value


class IDNode:
    def __init__(self, value):
        self.kind = value


class Parser:
    def __init__(self, tokens):
        print("Running Parser")
        self.tokens = tokens
        self.token_idx = 0
        self.current_token = self.tokens[self.token_idx]

    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]

    def parse(self):
        if len(self.tokens) < 1:
            print(f"One input at a time, sorry!\nUsing your first input: {self.tokens[0]}")
        tok = self.tokens[0]
        res = ParseResult()
        print(tok.getType())
        #  node = MockNode()  # Replace this with actual parsing logic if needed
        if tok.getType() == "KEYWORD":
            node = KWNode(tok.getVal())
        elif tok.getType() == "ID":
            node = IDNode(tok.getVal())
        elif tok.getType() == "INT":
            node = IntNode(tok.getVal())
        elif tok.getType == "FLOAT":
            node = FloatNode(tok.getVal())
        else:
            node = MockNode(tok.getVal())
        return res.success(node)


###################################
#####      INTERPRETER        #####
###################################

class Interpreter:
    def visit(self, node):
        print("Running Interpreter")
        method_name = f'visit_{type(node).__name__}'
        print(method_name)
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_MockNode(self, node):
        return node

    def visit_KWNode(self, node):
        return node

    def visit_IDNode(self, node):
        return node

    def visit_IntNode(self, node):
        return node

    def visit_float(self, node):
        return node


###################################
#####   BANK-ACCOUNT CLASS    #####
###################################

class BankAccount:
    account_number_counter = 1

    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.account_number = self.generate_account_number(first_name, last_name)
        BankAccount.account_number_counter += 1
        # Make account ID, 1->99999

    def generate_account_number(self, first_name, last_name):
        account_number = f"{first_name[0].upper()}{last_name[0].upper()}{self.account_number_counter:06d}"
        return account_number

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        add = 0
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            else:
                add = amount
        except ValueError as V:
            print(f"{type(V)}: {V}\nAttempted deposit of {amount} to {self.balance}")
        finally:
            self.balance += add

    def withdraw(self, amount):
        subtract = 0
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            elif amount > self.balance:
                raise ValueError("Withdrawal amount must be less than or equal to balance")
            else:
                subtract = amount
        except ValueError as V:
            print(f"{type(V)}: {V}\nAttempted withdrawal of {amount} from {self.balance}")
        finally:
            self.balance -= subtract

    @staticmethod
    def create_account(accounts, first_name, last_name, balance):
        new_account = BankAccount(first_name, last_name, balance)
        accounts.append(new_account)

    @staticmethod
    def get_account_by_id(accounts, account_id):
        for account in accounts:
            if account.get_account_number() == account_id:
                return account
        return None


###################################
#####         MAIN            #####
###################################

def main():
    # Accounts are live
    accounts = [
        BankAccount("Chris", "Ennis", 1000),
        BankAccount("James", "Vo", 2500),
        BankAccount("Keagan", "Haar", 750),
        BankAccount("Clark", "Kent", 950),
        BankAccount("Bruce", "Wayne", 7500000)
    ]
    MARK("Accounts:")  # Print
    for account in accounts:
        MARK(account.get_name() + " - " + account.get_account_number())

    # Make new account?
    if input("Create new account? (yes/no): ").lower() == "yes":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        balance = float(input("Initial deposit: "))
        BankAccount.create_account(accounts, first_name, last_name, balance)
        MARK("Account created!")
        MARK("Accounts:")
        for account in accounts:
            MARK(account.get_name() + " - " + account.get_account_number())

    # Get account by ID
    selected_account = None
    while not selected_account:
        temp = input("Enter account ID: ")
        account_id = run(temp)
        selected_account = BankAccount.get_account_by_id(accounts, account_id)
        if not selected_account:
            MARK("Invalid ID. Try again.")

    running = True
    while running:
        # Program Loop
        MARK("Selected: " + selected_account.get_name() + " - " + selected_account.get_account_number())
        MARK("Deposit")
        MARK("Withdrawal")
        MARK("1. Balance")
        MARK("2. Different account")
        MARK("3. Exit")

        choice = input("Choice: ")

        if run(choice) == "Deposit":
            amount = float(run(input("Deposit: ")))
            selected_account.deposit(amount)
        elif run(choice) == "Withdrawal":
            amount = float(run(input("Withdraw: ")))
            selected_account.withdraw(amount)
        elif choice == "1":
            MARK("Balance: $" + str(selected_account.get_balance()))
        elif choice == "2":
            selected_account = None
            while not selected_account:
                account_id = run(input("Enter account ID: "))
                selected_account = BankAccount.get_account_by_id(accounts, account_id)
                if not selected_account:
                    MARK("Invalid ID. Try again.")
        elif choice == "3" or choice.lower() == "exit":
            running = False
        else:
            MARK("Invalid choice. Try again.")

    MARK("Thank you for using V.E.H Brothers Superhero Bank")


def run(text):
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    result = interpreter.visit(ast.node)
    return result.kind


# Execute the main function
if __name__ == "__main__":
    main()
