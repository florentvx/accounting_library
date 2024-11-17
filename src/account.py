from __future__ import annotations
from typing import Any

from .account_path import account_path

class account:
    def __init__(
            self,
            name: str,
            unit: str,
            *,
            value: float | None = None,
            sub_accounts: list[account] | None = None
        ):
        
        if (value is None and sub_accounts is None):
            raise ValueError("Account has to be terminal or intemediary")
        elif ((value is not None) and (sub_accounts is not None)):
            raise ValueError("Account cannot be terminal and intermediary at the same time")
        elif not isinstance(name, str) or name == "":
            raise ValueError(f"account name is not set properly [{name}]")
        
        self.name: str = name
        self.unit : str = unit
        self.value: float | None = value
        self.sub_accounts : list[account] | None = sub_accounts

    @property
    def is_terminal(self):
        return self.value is not None

    def set_value(self, new_value):
        if not self.is_terminal:
            raise ValueError("cannot set value on a intermediary account")
        self.value = new_value

    def get_account(self, path: account_path | None):
        if path is None or path.is_empty:
            return self
        # if path.root_folder not in [x.name for x in self.sub_accounts]:
        #     raise ValueError(f"your account path {path} does refer to an unisting sub_account {path.root_folder}")
        # child_path = path.get_child()
        sa_match_list = [sa for sa in self.sub_accounts if sa.name.upper() == path.root_folder.upper()]
        if len(sa_match_list) == 0:
            raise ValueError(f"No match for subaccount {path.root_folder}")
        elif len(sa_match_list) > 1:
            raise ValueError(f"Multiple matches for {path.root_folder}")
        else:
            return sa_match_list[0].get_account(path.get_child())

    def get_account_structure(
            self, 
            prefix: account_path | None = None
        ) -> tuple[account_path, Any]:
        if prefix is None:
            prefix = account_path()
        full_prefix = prefix / self.name
        if self.is_terminal:
            return (full_prefix, None)
        return (
            full_prefix, 
            [
                sa.get_account_structure(full_prefix)
                for sa in self.sub_accounts
            ]
        )

    def _print_structure(self, structure, level):
        acc_p, rest_struct = structure
        acc_p: account_path
        if rest_struct is None:
            acc = self.get_account(acc_p.get_child())
            yield f"{'  ' * level} {level}. {acc_p} -> {acc.value} {acc.unit}"
        else:    
            yield f"{'  ' * level} {level}. {acc_p}"
            for child in rest_struct:
                for y in self._print_structure(child, level + 1):
                    yield y

    def print_structure(self, do_print: bool = True) -> str:
        res = ""
        for x in self._print_structure(structure = self.get_account_structure(), level=0):
            res += x + "\n"
            print(x)
        return res

    def _get_account_value(self, unit: str|None = None):
        if unit is None:
            unit = self.unit
        if self.is_terminal:
            if unit != self.unit:
                raise ValueError(f"not implemeted yet conversion between {unit} and {self.unit}")
            return self.value
        return sum([
            sa._get_account_value(self.unit)
            for sa in self.sub_accounts
        ])
    
    def _get_account_summary(self, unit):
        if unit is None:
            unit = self.unit
        if self.is_terminal:
            raise ValueError()
        else:
            return [
                [sa.name, sa._get_account_value(unit)] 
                for sa in self.sub_accounts
            ]
    
    def get_account_value(self, path: account_path = None, unit: str = None):
        return self.get_account(path)._get_account_value(unit)
    
    def get_account_summary(self, path: account_path = None, unit: str = None):
        return self.get_account(path)._get_account_summary(unit)
    
    def add_account(self, path: account_path, is_terminal: bool, unit: str = None):
        sub_acc = self.get_account(path.parent)
        if sub_acc.is_terminal:
            raise ValueError("cannot add account to a terminal account")
        test_l = [sa for sa in sub_acc.sub_accounts if sa.name == path.name]
        if len(test_l) != 0:
            raise ValueError()
        unit_to_use = unit if (not unit is None) else sub_acc.unit
        if is_terminal:
            sub_acc.sub_accounts += [account(path.name, value=0, unit=unit_to_use)]
        else:
            sub_acc.sub_accounts += [account(path.name, sub_accounts=[], unit=unit_to_use)]
        
        

