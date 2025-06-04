account = 0;
def create_account_for_user(user_balance):

            if user_balance <= 100:
                print("Balance must be greater than N100.")
            account = user_balance
            return account

def user_transactions(withdrawal_amount, account):
            if withdrawal_amount % 500 != 0 and withdrawal_amount % 1000 != 0:
                raise ValueError("Please enter an amount that is a multiple of 500 or 1000.")
            elif withdrawal_amount > account:
                print("Insufficient funds. Please enter a valid amount.")

            elif withdrawal_amount > 20000:
                print("The maximum amount you can withdraw at once is N20,000.")

            account = (withdrawal_amount - 100)
            print(f"Transaction successful. You withdrew {withdrawal_amount}.")
            print(f'withdral fee is: N100')
            print(f"Transaction successful. Your new balance is N{account}.")
            return account




def create_account_for_user(user_balance):
    global account
    if user_balance <= 100:
        print("Balance must be greater than N100.")
    account = user_balance
    return account


def user_transactions(withdrawal_amount, account):
    if withdrawal_amount % 500 != 0 and withdrawal_amount % 1000 != 0:
        raise ValueError("Please enter an amount that is a multiple of 500 or 1000.")
    elif withdrawal_amount > account:
        print("Insufficient funds. Please enter a valid amount.")
    elif withdrawal_amount > 20000:
        print("The maximum amount you can withdraw at once is N20,000.")
    elif withdrawal_amount > 0.9 * account:
        print("Error: Cannot withdraw more than 90% of the balance.")
    else:
        account -= (withdrawal_amount + 100)  # Subtract withdrawal amount and fixed fee
        print(f"Withdrawal successful. You withdrew {withdrawal_amount}.")
        print(f"Withdrawal fee is: N100")
        print(f"Your new balance is N{account}.")
    return account


import unittest
from unittest.mock import patch
import function_bank

class TestBankApp(unittest.TestCase):

    @patch('builtins.print')
    def test_create_account_for_user(self, mock_print):
        balance = 50000
        actual = function_bank.create_account_for_user(balance)
        expected = 50000
        self.assertEqual(actual, expected)
        mock_print.assert_not_called()  # Ensure no print was called

    @patch('builtins.print')
    def test_user_transactions_valid(self, mock_print):
        account = 50000
        withdrawal_amount = 20000
        actual = function_bank.user_transactions(withdrawal_amount, account)
        expected = 20000
        self.assertEqual(actual, expected)
        mock_print.assert_any_call(f"Withdrawal successful. You withdrew {withdrawal_amount}.")
        mock_print.assert_any_call(f"Withdrawal fee is: N100")
        mock_print.assert_any_call(f"Your new balance is N{expected}.")

    @patch('builtins.print')
    def test_user_transactions_insufficient_funds(self, mock_print):
        account = 50000
        withdrawal_amount = 60000
        actual = function_bank.user_transactions(withdrawal_amount, account)
        expected = 50000
        self.assertEqual(actual, expected)
        mock_print.assert_any_call("Insufficient funds. Please enter a valid amount.")

    @patch('builtins.print')
    def test_user_transactions_over_20000(self, mock_print):
        account = 50000
        withdrawal_amount = 25000
        actual = function_bank.user_transactions(withdrawal_amount, account)
        expected = 50000
        self.assertEqual(actual, expected)
        mock_print.assert_any_call("The maximum amount you can withdraw at once is N20,000.")

    @patch('builtins.print')
    def test_user_transactions_over_90_percent(self, mock_print):
        account = 50000
        withdrawal_amount = 46000
        actual = function_bank.user_transactions(withdrawal_amount, account)
        expected = 50000
        self.assertEqual(actual, expected)
        mock_print.assert_any_call("Error: Cannot withdraw more than 90% of the balance.")

    @patch('builtins.print')
    def test_user_transactions_valid_with_fee(self, mock_print):
        account = 50000
        withdrawal_amount = 10000
        expected_balance = 39000  # 50000 - 10000 - 100 (fee)
        actual = function_bank.user_transactions(withdrawal_amount, account)
        self.assertEqual(actual, expected_balance)
        mock_print.assert_any_call(f"Withdrawal successful. You withdrew {withdrawal_amount}.")
        mock_print.assert_any_call(f"Withdrawal fee is: N100")
        mock_print.assert_any_call(f"Your new balance is N{expected_balance}.")

if __name__ == '__main__':
    unittest.main()
