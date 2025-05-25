import function_bank
from unittest.mock import patch
import unittest

class TestBankFunction(unittest.TestCase):
    def test_that_function_exist(self):
         name = "tega"
         bal = 0.0
         account = function_bank.open_account(name, bal)
         self.assertEqual(account[0], name)
         self.assertEqual(account[2], bal)


    @patch('random.randint')
    def test_account_number_range(self, mock_randint):
        mock_randint.return_value = 9876543210
        account = function_bank.open_account("Jane Smith", 500.0)
        self.assertGreaterEqual(account[1], 1000000000)
        self.assertLessEqual(account[1], 9999999999)

    def test_empty_name(self):
        account = function_bank.open_account("", 1000.0)
        self.assertEqual(account[0], "")
        self.assertEqual(account[2], 1000.0)


    def test_large_balance(self):
        account = function_bank.open_account("Jane Smith", 1e6)
        self.assertEqual(account[0], "Jane Smith")
        self.assertEqual(account[2], 1e6)

    def test_multiple_account_creations(self):
        account1 = function_bank.open_account("Alice Johnson")
        account2 = function_bank.open_account("Bob Brown")
        self.assertNotEqual(account1[1], account2[1])

    def test_account_number_format(self):
        account = function_bank.open_account("Eve Foster")
        self.assertIsInstance(account[1], int)
        self.assertEqual(len(str(account[1])), 10)

    def test_negative_balance(self):
        with self.assertRaises(ValueError):
            function_bank.open_account("John Doe", -500.0)


    def setUp(self):
        self.account = function_bank.open_account("John Doe", 1000.0)


    def test_valid_deposit(self):
        new_balance = function_bank.deposit(self.account, 500.0)
        self.assertEqual(new_balance, 1500.0)
        self.assertEqual(self.account[2], 1500.0)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            function_bank.deposit(self.account, 0.0)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            function_bank.deposit(self.account, -100.0)

    def test_deposit_empty_string(self):
        with self.assertRaises(ValueError):
            function_bank.deposit(self.account, "")

    def test_deposit_non_numeric_string(self):
        with self.assertRaises(ValueError):
            function_bank.deposit(self.account, "abc")

    def test_deposit_whitespace_string(self):
        with self.assertRaises(ValueError):
            function_bank.deposit(self.account, "   ")

    def test_deposit_float(self):
        new_balance = function_bank.deposit(self.account, 150.75)
        self.assertEqual(new_balance, 1150.75)
        self.assertEqual(self.account[2], 1150.75)

    def test_deposit_large_amount(self):
        new_balance = function_bank.deposit(self.account, 1e6)
        self.assertEqual(new_balance, 1001000.0)
        self.assertEqual(self.account[2], 1001000.0)

