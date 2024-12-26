from src.asset import asset

EUR = asset("EUR", "€")
USD = asset("USD", "$")
GBP = asset("GBP", "£")
JPY = asset("JPY", "¥", separator_param=4, decimal_param=0)


def test_asset():

    assert GBP.show_value(123456.123456) == "£ 123,456.12"
    assert JPY.show_value(12345678.926456) == "¥ 1234,5679"
    assert USD.show_value(-9999.999) == "- $ 10,000"