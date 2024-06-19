import unittest
#from banking import Bank, Customer, Account


class TestBankingDSL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass\n')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass\n')

    def setUp(self):
        print('setUp')
        self.bank = Bank()
        self.Chris = Customer(first_name="Chris", last_name="Ennis")
        self.bank.add_customer(self.Chris)
        self.checking_account = Account(owner=self.Chris)
        self.Chris.open_account(self.checking_account)

    def tearDown(self):
        print('tearDown\n')

    def test_deposit(self):
        print('test_deposit')
        self.checking_account.transact('deposit', 200.00)
        self.assertEqual(self.checking_account.transaction_count(), 1)
        self.assertEqual(self.checking_account.current_balance(), 200.00)

    def test_withdrawal(self):
        print('test_withdrawal')
        self.checking_account.transact('deposit', 200.00)
        self.checking_account.transact('withdrawal', 150.00)
        self.assertEqual(self.checking_account.transaction_count(), 2)
        self.assertEqual(self.checking_account.current_balance(), 50.00)

    def test_account_number_generation(self):
        print('test_account_number_generation')
        account_number = self.checking_account.account_number
        self.assertTrue(account_number.startswith("CE"))
        self.assertEqual(len(account_number), 8)

    def test_balance_error(self):
        print('test_balance_error')
        self.checking_account.transact('deposit', 50.00)
        with self.assertRaises(ValueError):
            self.checking_account.transact('withdrawal', 100.00)

    def test_invalid_transaction_type(self):
        print('test_invalid_transaction_type')
        with self.assertRaises(ValueError):
            self.checking_account.transact('invalid_type', 100.00)


if __name__ == '__main__':
    unittest.main()
