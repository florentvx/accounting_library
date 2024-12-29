from .account_path import test_account_path
from .asset import test_asset
from .account import test_account
from .fx_market import test_fx_market

def run_all_tests():
    print("Running account_path test")
    test_account_path()
    print("Running asset test")
    test_asset()
    print("Running fx_market test")
    test_fx_market()
    print("Running account test")
    test_account()
