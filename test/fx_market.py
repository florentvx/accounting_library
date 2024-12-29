from src.asset import asset
from src.fx_market import fx_market

from test.asset import EUR, GBP, JPY, USD

FXM = fx_market()
FXM.add_quote(EUR, USD, 1.05)
FXM.add_quote(GBP, JPY, 200)
FXM.add_quote(GBP, USD, 1.5)

def test_fx_market():

    assert not FXM.add_quote(EUR, JPY, 100)
    assert FXM.get_quote(EUR, EUR) == 1.0
    assert abs(FXM.get_quote(USD, EUR) - 1.0 / 1.05) < 10 ** -5
    assert abs(FXM.get_quote(GBP, EUR) - 1.5 / 1.05) < 10 ** -5
    assert abs(FXM.get_quote(EUR, JPY) - 1.05 / 1.5 * 200) < 10 ** -5

    #EURJPY = FXM.get_quote(EUR, JPY)
