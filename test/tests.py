from banking import *
import unittest


class SpecificationTest(unittest.TestCase):
    def setUp(self):
        self.test_account = BankAccount("Bruce", "Wayne", 500)
        self.testBank = BankSys()
        self.accounts = []

    def tearDown(self):
        del self.test_account
        del self.accounts

    def test_withdrawal(self):
        # Test withdrawing an amount from the account reduces the balance correctly.
        initial_balance = self.test_account.get_balance()
        withdrawal_amount = 200
        self.test_account.withdraw(withdrawal_amount)
        new_balance = self.test_account.get_balance()
        try:
            self.assertEqual(float(new_balance), float(initial_balance) - float(withdrawal_amount))
            print("PASSED: Withdrawal")
        except AssertionError:
            print("FAILED: Withdrawal")

    def test_deposit(self):
        # Test depositing an amount into the account increases the balance correctly.
        initial_balance = self.test_account.get_balance()
        deposit_amount = 300
        self.test_account.deposit(deposit_amount)
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
        self.testBank.create_account("Clark", "Kent", 3000)
        self.testBank.create_account("Kal", "El", 5000)
        try:
            self.assertEqual(len(self.testBank.accounts), 7)
            print("PASSED: Account creation")
        except AssertionError:
            print("FAILED: Account creation")


if __name__ == '__main__':
    unittest.main()
