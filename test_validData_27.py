from dev_rev_list import *
import validData_27

def test_validData_27():

    pr_list = validData_27.validData_27("STQ_Database", "giraph", "a/b/c/")

    assert 'p4' in pr_list
    assert 'p6' in pr_list
    assert 'p1' not in pr_list
    