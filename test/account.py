from __future__ import annotations
from src import account, account_path

def test_account():

    acc = account("acc", value = 100)
    acc_empty = account("acc_sv_2", sub_accounts=[])
    acc_sa01 = account("sa01", value = 12)
    acc_2 = account("acc2", sub_accounts=[
        account("sa0", value = 102),
        account("sa1", sub_accounts= [
            account("sa00", value = 52),
            acc_sa01,
        ]),
        account("sa3", sub_accounts=[
            account("x", value=100000),
            account("x", sub_accounts=[]),
        ]),
    ])

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

    terminal = account("singleton", value=10)
    assert terminal.is_terminal

    intermediary_empty = account("int_empty", sub_accounts=[])
    assert not intermediary_empty.is_terminal

    #endregion

    #region set_value
    
    acc1 = account("acc_sv_1", value=0)
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
    except:
        test_ga_4 = True
    assert test_ga_4

    #endregion

    #region get_account_structure
    
    test_ = acc_2.get_account_structure(None)
    assert str(test_) == "(account_path('acc2'), " + \
        "[(account_path('acc2/sa0'), None), (account_path('acc2/sa1'), " + \
        "[(account_path('acc2/sa1/sa00'), None), (account_path('acc2/sa1/sa01'), None)]), (account_path('acc2/sa3'), " + \
        "[(account_path('acc2/sa3/x'), None), (account_path('acc2/sa3/x'), [])])])"

    #endregion