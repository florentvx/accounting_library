from __future__ import annotations
import datetime as dt
from .account_path import account_path
from .asset import asset
from .fx_market import fx_market
from .account import account

def initialize_statement(unit: asset):
    return statement(dt.datetime.now(), fx_market(), account(unit=unit))

class statement:
    def __init__(
            self, 
            date: dt.datetime, 
            fx_mkt: fx_market, 
            acc: account,
        ):
        self.date : dt.datetime = date
        self.fx_market : fx_market = fx_mkt
        self.account : account = acc
        self.print_summary(do_print=False) # forces the computation of all fx quotes needed
    
    def copy_statement(self, date: dt.datetime):
        return statement(date, self.fx_market.copy(), self.account.copy())
    
    def get_account(self, ap: account_path) -> account:
        return self.account.get_account(ap)
    
    def change_terminal_account(
            self, 
            ap: account_path, 
            value: float|None = None, 
            unit: asset|None = None,
        ) -> None:
        acc = self.get_account(ap)
        if acc.is_terminal:
            if value is not None:
                acc.value=value
            if unit is not None:
                acc.unit=unit 
        else:
            raise ValueError(f"account: [{acc}] is not terminal")
        
    def change_folder_account(self, ap:account_path, unit: asset):
        acc = self.get_account(ap)
        if not acc.is_terminal:
            if unit is not None:
                acc.unit=unit 
        else:
            raise ValueError(f"account: [{acc}] is terminal")
    
    def print_structure(self, do_print: bool = False) -> str:
        res = self.account.print_structure(do_print=False) + "\n" + str(self.fx_market)
        if do_print:
            print(res)
        return res
    
    def print_summary(self, path: account_path = None, unit: asset = None, do_print: bool = False):
        res = f"Statement: {self.date.date().isoformat()}\n"
        res += self.account.print_account_summary(self.fx_market, path, unit, do_print=False)
        if do_print:
            print(res)
        return res