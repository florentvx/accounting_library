import datetime as dt

from src import statement, account, account_path

from .fx_market import FXM, EUR, USD, JPY, GBP

def test_statement():
    acc_test = account("root", unit=EUR, 
        sub_accounts=[
            account("europe", unit=EUR, 
                sub_accounts=[
                    account("my_bank", unit=EUR, value=1000),
                    account("my_loan", unit=EUR, value=-100)
                ]
            ),
            account("usa", unit=USD,
                sub_accounts=[
                    account("my_bank", unit=USD, value=250),
                    account("my_investment", unit=USD, value=145600.2)
                ]
            )
        ]
    )

    my_state = statement(dt.datetime(2025,1,5), FXM, acc_test)

    my_state2=my_state.copy_statement(dt.datetime(2025,2,5))
    my_state3=my_state.copy_statement(dt.datetime(2025,3,5))
    my_state4=my_state.copy_statement(dt.datetime(2025,4,5))

    my_state2.change_terminal_account(account_path("europe/my_bank"),value=100)
    my_state3.change_terminal_account(account_path("usa/my_investment"), value=123456, unit=JPY)
    my_state4.change_folder_account(account_path("europe"), unit=GBP)    

    ps1 = my_state.print_summary(do_print=True)
    ps2 = my_state2.print_summary(do_print=True)
    ps3 = my_state3.print_summary(do_print=True)
    ps4 = my_state4.print_summary(do_print=True)
    
    test = False
    try:
        my_state3.change_terminal_account(account_path("usa"), unit=EUR)
    except ValueError as e:
        print(e)
        test = True
    assert test
    print("END")