from src.fx_market import asset, fx_market

eur = asset("EUR", "€")
usd = asset("USD", "$")
gbp = asset("GBP", "£")
jpy = asset("JPY", "¥", separator_param=4, decimal_param=0)

assert gbp.show_value(123456.123456) == "£ 123,456.12"
assert jpy.show_value(12345678.926456) == "¥ 1234,5679"
assert usd.show_value(-9999.999) == "- $ 10,000"


fxm = fx_market()
fxm.add_quote(eur, usd, 1.05)
fxm.add_quote(gbp, jpy, 200)
fxm.add_quote(gbp, usd, 1.5)

assert not fxm.add_quote(eur, jpy, 100)
assert fxm.get_quote(eur, eur) == 1.0
assert abs(fxm.get_quote(usd, eur) - 1.0 / 1.05) < 10 ** -5
assert abs(fxm.get_quote(gbp, eur) - 1.5 / 1.05) < 10 ** -5
assert abs(fxm.get_quote(eur, jpy) - 1.05 / 1.5 * 200) < 10 ** -5


#eurjpy = fxm.get_quote(eur, jpy)

print("END")