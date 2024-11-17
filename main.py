from src import *

a1 = account("a1", value = 100, unit="EUR")
a2 = account("a2", value = 50, unit="EUR")
a = account("a", sub_accounts=[a1,a2], unit="EUR")
b= account(name="b", value=123, unit="EUR")
root = account("root", sub_accounts=[a,b], unit="EUR")

res = root.get_account(account_path('a/a1'))
popo = root.get_account_structure()
root.print_structure()

summary = root.get_account_summary()

root.add_account(account_path('c'),is_terminal=True)
root.add_account(account_path('a/a_0'),is_terminal=False)
root.add_account(account_path('a/a_0/this is good'),is_terminal=True)

root.print_structure()

print("END")