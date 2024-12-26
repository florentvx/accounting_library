from src.asset import asset
from src.fx_market import fx_market

from test.asset import EUR, GBP, JPY, USD

def test_fx_market():

    fxm = fx_market()
    fxm.add_quote(EUR, USD, 1.05)
    fxm.add_quote(GBP, JPY, 200)
    fxm.add_quote(GBP, USD, 1.5)

    assert not fxm.add_quote(EUR, JPY, 100)
    assert fxm.get_quote(EUR, EUR) == 1.0
    assert abs(fxm.get_quote(USD, EUR) - 1.0 / 1.05) < 10 ** -5
    assert abs(fxm.get_quote(GBP, EUR) - 1.5 / 1.05) < 10 ** -5
    assert abs(fxm.get_quote(EUR, JPY) - 1.05 / 1.5 * 200) < 10 ** -5

    #EURJPY = fxm.get_quote(EUR, JPY)
