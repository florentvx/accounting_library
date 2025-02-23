import unittest
import datetime as dt

from src import statement, account, account_path

from test.test_asset import EUR, USD, JPY, GBP
from test.test_fx_market import FXM

ACC_TEST = account("root", unit=EUR, 
        sub_accounts=[
            account("europe", unit=EUR, 
                sub_accounts=[
                    account("my_bank", unit=EUR, value=1000),
                    account("my_loan", unit=EUR, value=-100)
                ]
            ),
            account("usa", unit=USD,
                sub_accounts=[
                    account("my_bank", unit=USD, value=250),
                    account("my_investment", unit=USD, value=145600.2)
                ]
            )
        ]
    )

class TestStatement(unittest.TestCase):

    def setUp(self):
        self.my_state = statement(dt.datetime(2025,1,5), FXM, ACC_TEST)
        self.my_state2=self.my_state.copy_statement(dt.datetime(2025,2,5))
        self.my_state3=self.my_state.copy_statement(dt.datetime(2025,3,5))
        self.my_state4=self.my_state.copy_statement(dt.datetime(2025,4,5))

    def test_copy_statement(self):
        self.assertEqual(self.my_state.date, dt.datetime(2025,1,5))
        self.assertEqual(self.my_state2.date, dt.datetime(2025,2,5))
        self.assertEqual(self.my_state3.date, dt.datetime(2025,3,5))
        self.assertEqual(self.my_state4.date, dt.datetime(2025,4,5))

    def test_change_terminal_account(self):
        self.my_state2.change_terminal_account(account_path("europe/my_bank"), value=100)
        self.assertEqual(self.my_state2.get_account(account_path("europe/my_bank")).value, 100)

        self.my_state3.change_terminal_account(account_path("usa/my_investment"), value=123456, unit=JPY)
        self.assertEqual(self.my_state3.get_account(account_path("usa/my_investment")).value, 123456)
        self.assertEqual(self.my_state3.get_account(account_path("usa/my_investment")).unit, JPY)

    def test_change_folder_account(self):
        self.my_state4.change_folder_account(account_path("europe"), unit=GBP)
        self.assertEqual(self.my_state4.get_account(account_path("europe")).unit, GBP)

    def test_invalid_change_terminal_account(self):
        with self.assertRaises(ValueError):
            self.my_state3.change_terminal_account(account_path("usa"), unit=EUR)

    def test_print_summary(self):
        ps1 = self.my_state.print_summary(do_print=True)
        self.my_state2.change_terminal_account(account_path("europe/my_bank"), value=100)
        ps2 = self.my_state2.print_summary(do_print=True)
        self.my_state3.change_terminal_account(account_path("usa/my_investment"), value=123456, unit=JPY)
        ps3 = self.my_state3.print_summary(do_print=True)
        self.my_state4.change_folder_account(account_path("europe"), unit=GBP)
        ps4 = self.my_state4.print_summary(do_print=True)

        self.assertIsNotNone(ps1)
        self.assertIsNotNone(ps2)
        self.assertIsNotNone(ps3)
        self.assertIsNotNone(ps4)
        
