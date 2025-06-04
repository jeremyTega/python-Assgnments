import function_bank
from unittest.mock import patch
import unittest


class Testbankapp(unittest.TestCase):
    def test_create_account_for_user(self):
         balance = 50000
         actual = function_bank.create_account_for_user(balance)
         expected = 50000
         self.assertEqual(actual, expected)

    def test_userTransction(self):
         withdrawal_amount = 25000
         account = 50000
         actual = function_bank.user_transactions(withdrawal_amount, account)
         expected = 20000
         self.assertEqual(actual, expected)

    def test_exceeds_balance(self):
          account = 50000
          withdrawal = 20000
          actual = function_bank.user_transactions(withdrawal, account)
          expected = 29000
          self.assertEqual(actual, expected)

    def test_percent(self):
        self.assertEqual(
            function_bank.user_transactions(1000, 950),
            "Error: Cannot withdraw more than 90% of the balance."
        )

    def test_over_20000_percent(self):
            self.assertEqual(
                function_bank.user_transactions(1000, 210000),
                "Error: Withdrawal exceeds 20000% of the balance."
            )

    def test_exact_90_percent(self):
        self.assertEqual(
            function_bank.user_transactions(1000, 900),
            "Withdrawal successful. New balance: 100.0"
        )




