###################################
#####        CONSTANTS        #####
###################################

DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
MARK = print


###################################
#####          ERRORS         #####
###################################

class BankError(Exception):
    pass


class InvalidAccountIDError(BankError):
    def __init__(self, account_id):
        self.message = f"Invalid account ID: {account_id}"
        super().__init__(self.message)


class OverDrawException(BankError):
    def __init__(self, account_id):
        self.message = f"Invalid account ID: {account_id}"
        super().__init__(self.message)


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
    'def', 'MARK', 'IF', 'ELSE', 'ENDIF', 'WHILE', 'ENDWHILE'
]


###################################
#####         LEXER           #####
###################################

# Initialize Tokens
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value


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
    pass


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
        res = ParseResult()
        node = MockNode()  # Replace this with actual parsing logic if needed
        return res.success(node)


###################################
#####      INTERPRETER        #####
###################################

class Interpreter:
    def visit(self, node):
        print("Running Interpreter")
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_MockNode(self, node):
        return "Interpreted Mock Node"  # Simplified for demonstration purposes


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
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

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
    accounts = [
        BankAccount("Chris", "Ennis", 1000),
        BankAccount("James", "Vo", 2500),
        BankAccount("Keagan", "Haar", 750),
        BankAccount("Clark", "Kent", 950),
        BankAccount("Bruce", "Wayne", 7500000)
    ]

    MARK("Accounts:")
    for account in accounts:
        MARK(account.get_name() + " - " + account.get_account_number())

    if input("Create new account? (yes/no): ").lower() == "yes":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        balance = float(input("Initial deposit: "))
        BankAccount.create_account(accounts, first_name, last_name, balance)
        MARK("Account created!")
        MARK("Accounts:")
        for account in accounts:
            MARK(account.get_name() + " - " + account.get_account_number())

    # Lexer, Parser, Interpreter demonstration
    text = "some sample text"
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    result = interpreter.visit(ast.node)

    selected_account = None
    while not selected_account:
        account_id = input("Enter account ID: ")
        selected_account = BankAccount.get_account_by_id(accounts, account_id)
        if not selected_account:
            MARK("Invalid ID. Try again.")

    running = True
    while running:
        MARK("Selected: " + selected_account.get_name() + " - " + selected_account.get_account_number())
        MARK("1. Deposit")
        MARK("2. Withdraw")
        MARK("3. Balance")
        MARK("4. Different account")
        MARK("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            amount = float(input("Deposit: "))
            selected_account.deposit(amount)
        elif choice == "2":
            amount = float(input("Withdraw: "))
            selected_account.withdraw(amount)
        elif choice == "3":
            MARK("Balance: $" + str(selected_account.get_balance()))
        elif choice == "4":
            selected_account = None
            while not selected_account:
                account_id = input("Enter account ID: ")
                selected_account = BankAccount.get_account_by_id(accounts, account_id)
                if not selected_account:
                    MARK("Invalid ID. Try again.")
        elif choice == "5" or choice.lower() == "exit":
            running = False
        else:
            MARK("Invalid choice. Try again.")

    MARK("Thank you for using VEH Bank")


# Execute the main function
if __name__ == "__main__":
    main()
