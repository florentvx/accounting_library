from src import *

EUR = asset("EUR", "€")
USD = asset("USD", "$")
GBP = asset("GBP", "£")
JPY = asset("JPY", "¥", separator_param=4, decimal_param=0)

FXM = fx_market()
FXM.add_quote(EUR, USD, 1.05)
FXM.add_quote(GBP, JPY, 200)
FXM.add_quote(GBP, USD, 1.5)


a1 = account("a1", unit=EUR, value = 100)
a2 = account("a2", unit=EUR, value = 50)
a = account("a", unit=EUR, sub_accounts=[a1,a2])
b1 = account("b1", unit=JPY, value=25000)
b2 = account("b2", unit=USD, value=150)
b= account(name="b", unit=EUR, sub_accounts=[b1, b2])
root = account("root", unit=GBP, sub_accounts=[a,b])

res = root.get_account(account_path('a/a1'))
popo = root.get_account_structure()
root.print_structure(do_print=True)

summary = root.get_account_summary(FXM)
root.print_account_summary(FXM, do_print=True)
root.get_account(account_path('b')).print_account_summary(FXM, do_print=True)

root.add_account(account_path('c'), is_terminal=True)
root.add_account(account_path('a/a_0'), unit=JPY, is_terminal=False)
root.add_account(account_path('a/a_0/this is good'), unit=USD, is_terminal=True)

root.print_structure(do_print=True)
root.print_account_summary(FXM, do_print=True)

print("END")