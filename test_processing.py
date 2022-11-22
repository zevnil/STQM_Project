from processing import *
from dev_rev_list import *
from validData_26 import *

def test_processing():
    dev, rev, uq_map = dev_rev_list("STQ_Database", "giraph")
    valid_prs = validData_26("STQ_Database", "giraph")
    actual_xt, actual_yt, actual_zt = processing("STQ_Database", valid_prs, dev, rev, uq_map)
    assert actual_xt['fd3'] == 4.59178233441104e-41
    assert actual_xt['fd5'] == 4.59178233441104e-41
    assert actual_xt['fd1'] == 0
    assert actual_xt['fd4'] != 9.269031119592087e-221
    assert actual_yt[0] == 1.6278159311829022e-66
    assert actual_yt[1] == 3.9338885003586806e-66
    assert actual_yt[2] == 3.9338885003586806e-66
    assert 5 not in actual_yt
    assert actual_zt['fd10'] == 4.360169587945797e-106
    assert actual_zt['fd11'] == 4.360169587945797e-106
    assert actual_zt['fd8'] == 0
    assert 'fd-1' not in actual_zt

