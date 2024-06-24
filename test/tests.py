from banking import *
import unittest


class SpecificationTest(unittest.TestCase):
    def setUp(self):
        self.test_account = BankAccount("Bruce", "Wayne", 500)
        #  self.testBank = BankSys()
        self.accounts = []

    def tearDown(self):
        del self.test_account
        del self.accounts

    def test_withdrawal(self):
        # Test withdrawing an amount from the account reduces the balance correctly.
        initial_balance = self.test_account.get_balance()
        print("Can get balance from test account.")
        withdrawal_amount = 200
        self.test_account.withdraw(withdrawal_amount)
        print("Can withdraw from test account.")
        new_balance = self.test_account.get_balance()
        try:
            self.assertEqual(float(new_balance), float(initial_balance) - float(withdrawal_amount))
            print("PASSED: Withdrawal")
        except AssertionError:
            print("FAILED: Withdrawal")

    def test_deposit(self):
        # Test depositing an amount into the account increases the balance correctly.
        initial_balance = self.test_account.get_balance()
        print("Can get balance from test account.")
        deposit_amount = 300
        self.test_account.deposit(deposit_amount)
        print("Can deposit to test account.")
        new_balance = self.test_account.get_balance()
        try:
            self.assertEqual(float(new_balance), float(initial_balance) + float(deposit_amount))
            print("PASSED: Deposit")
        except AssertionError:
            print("FAILED: Deposit")

    def test_account_id_creation(self):
        # Test that each account is assigned a unique account number.
        account1 = BankAccount("Wally", "West", 1000)
        account2 = BankAccount("Barry", "Allen", 2000)
        try:
            self.assertNotEqual(account1.get_account_number(), account2.get_account_number())
            print("PASSED: Account number creation")
        except AssertionError:
            print("FAILED: Account number creation")

    def test_account_creation(self):
        # Test that creating accounts adds them to the accounts list.
        test_accounts = [BankAccount("Clark", "Kent", 3000),
                         BankAccount("Kal", "El", 5000)]
        try:
            self.assertEqual(len(test_accounts), 2)
            print("PASSED: Account creation")
        except AssertionError:
            print("FAILED: Account creation")


if __name__ == '__main__':
    unittest.main()
