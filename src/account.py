from __future__ import annotations

from account_path import account_path

class account:
    def __init__(
            self,
            name: str,
            *,
            value: float = None,
            sub_accounts: list[account] = None
        ):
        
        if (value is None and sub_accounts is None):
            raise ValueError("Account has to be terminal or intemediary")
        elif ((value is not None) and (sub_accounts is not None)):
            raise ValueError("Account cannot be terminal and intermediary at the same time")
        elif isinstance(name, str) and name == "":
            raise ValueError(f"name is not set properly [{name}]")
        
        self.name: str = name
        self.value: float = value
        self.sub_accounts : list[account] = sub_accounts

    @property
    def is_terminal(self):
        return self.value is not None

    def set_value(self, new_value):
        if not self.is_terminal:
            raise ValueError("cannot set value on a intermediary account")
        self.value = new_value

    def get_account(self, path: account_path):
        if path.root_folder != self.name:
            raise ValueError("")
        if path.is_singleton:
            return self
        child_path = path.get_child()
        sa_match_list = [sa for sa in self.sub_accounts if sa.name == child_path.root_folder]
        if len(sa_match_list) == 0:
            raise ValueError()
        elif len(sa_match_list) > 1:
            raise ValueError()
        else:
            return sa_match_list[0].get_account(child_path)

    def get_account_structure(self, prefix: account_path = None):
        if prefix is None:
            prefix = account_path()
        full_prefix = prefix / self.name
        if self.is_terminal:
            return full_prefix
        return (
            full_prefix, 
            [
                sa.get_account_structure(full_prefix)
                for sa in self.sub_accounts
            ]
        )

    def _print_structure(self, structure, level):
        if isinstance(structure, account_path):
            print(f"{'  ' * level} {level}. {structure} -> {self.get_account(structure).value}")
        else:    
            print(f"{'  ' * level} {level}. {structure[0]}")
            for child in structure[1]:
                self._print_structure(child, level + 1)

    def print_structure(self):
        self._print_structure(structure = self.get_account_structure(), level=0)

a1 = account("a1", value = 100)
a2 = account("a2", value = 50)
a = account("a", sub_accounts=[a1,a2])
b= account(name="b", value=123)
root = account("root", sub_accounts=[a,b])

res = root.get_account(account_path('root/a/a1'))
popo = root.get_account_structure()
root.print_structure()
print("END")