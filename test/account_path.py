from __future__ import annotations
from src.account_path import account_path

def test_account_path():
    def test_path(my_path: str):
        ap = account_path(my_path)
        return f"{str(ap)}_{ap.is_empty}_{ap.is_singleton}_{ap.root_folder}_{str(ap.get_child())}"

    assert test_path("") == "._True_False_None_."
    assert test_path("root/a/b/c/") == "root/a/b/c_False_False_root_a/b/c"
    assert test_path("root2/z/y") == "root2/z/y_False_False_root2_z/y"
    assert test_path("folder") == "folder_False_True_folder_."

    test_failure = True
    # try:
    #     res = test_path(None)
    #     test_failure = False
    # except:
    #     pass
    try:
        res = test_path("/R3/1/5/")
        test_failure = False
    except:
        pass
    assert test_failure
    return