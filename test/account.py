from __future__ import annotations

from src.account_path import account_path
from src.asset import asset
from src.account import account

def test_account():

    eur = asset("EUR", "€")

    acc = account("acc", value = 100, unit=eur)
    acc_empty = account("acc_sv_2", sub_accounts=[], unit=eur)
    acc_sa01 = account("sa01", value = 12, unit = eur)
    acc_2 = account("acc2", sub_accounts=[
        account("sa0", value = 102, unit = eur),
        account("sa1", sub_accounts= [
            account("sa00", value = 52, unit = eur),
            acc_sa01,
        ], unit = eur),
        account("sa3", sub_accounts=[
            account("x", value=100000, unit = eur),
            account("y", sub_accounts=[], unit = eur),
        ], unit = eur),
    ], unit = eur)

    #region __init__

    test_error = True
    try:
        error = account("Error")
        test_error = False
    except:
        pass
    assert test_error

    test_error = True
    try:
        error = account("Error", value = None)
        test_error = False
    except:
        pass
    assert test_error


    test_error = True
    try:
        error = account("Error", sub_accounts=None)
        test_error = False
    except:
        pass
    assert test_error

    #endregion

    #region is_terminal

    terminal = account("singleton", value=10, unit=eur)
    assert terminal.is_terminal

    intermediary_empty = account("int_empty", sub_accounts=[], unit=eur)
    assert not intermediary_empty.is_terminal

    #endregion

    #region set_value
    
    acc1 = account("acc_sv_1", value=0, unit=eur)
    acc1.set_value(101)
    assert acc1.value == 101

    
    test_fail_sv = False
    try:
        acc_empty.set_value(101)
    except:
        test_fail_sv = True
    assert test_fail_sv
    
    #endregion

    #region get_account
    
    acc_p = account_path("a/x")
    acc_p2 = account_path("sa0/y")
    acc_p3 = account_path("Sa1/sA01")
    acc_p4 = account_path("sa3/x")

    x = acc_2.get_account(None)
    assert acc_2 == x

    assert acc == acc.get_account(None)
    assert acc == acc.get_account(account_path(""))

    test_ga_2 = False
    try:
        acc_2.get_account(acc_p)
    except:
        test_ga_2 = True
    assert test_ga_2

    test_ga_3 = False
    try:
        acc_2.get_account(acc_p2)
    except:
        test_ga_3 = True
    assert test_ga_3

    assert acc_2.get_account(acc_p3) == acc_sa01

    test_ga_4 = False
    try:
        acc_2.get_account(acc_p4)
        test_ga_4 = True
    except:
        test_ga_4 = False
    assert test_ga_4

    #endregion

    #region get_account_structure
    
    test_ = acc_2.get_account_structure(None)
    popo = acc_2.print_structure()
    assert popo == ' 0. acc2\n   1. acc2/sa0 -> 102 EUR\n   1. acc2/sa1\n     2. acc2/sa1/sa00 -> 52 EUR\n  '+\
        '   2. acc2/sa1/sa01 -> 12 EUR\n   1. acc2/sa3\n     2. acc2/sa3/x -> 100000 EUR\n     2. acc2/sa3/y\n'

    #endregion