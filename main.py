from src import *

ap = account_path('root/a/b/c/')
print(ap.name)
print(ap.parent)

ap2 = ap / "d"
print(ap2)
print(ap2.get_child())


a1 = account("a1", value = 100)
a2 = account("a2", value = 50)
a = account("a", sub_accounts=[a1,a2])
b= account(name="b", value=123)
root = account("root", sub_accounts=[a,b])

res = root.get_account(account_path('root/a/a1'))
popo = root.get_account_structure()
root.print_structure()

summary = root.get_account_summary()

print("END")