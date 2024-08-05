from src import *

a1 = account("a1", value = 100)
a2 = account("a2", value = 50)
a = account("a", sub_accounts=[a1,a2])
b= account(name="b", value=123)
root = account("root", sub_accounts=[a,b])

res = root.get_account(account_path('root/a/a1'))
popo = root.get_account_structure()
root.print_structure()

summary = root.get_account_summary()

root.add_account(account_path('root/c'),is_terminal=True)
root.add_account(account_path('root/a/a_0'),is_terminal=False)
root.add_account(account_path('root/a/a_0/this is good'),is_terminal=True)

root.print_structure()

print("END")