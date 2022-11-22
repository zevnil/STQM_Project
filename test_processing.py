from processing import *
from dev_rev_list import *
from validData_26 import *

def test_processing():
    dev, rev, uq_map = dev_rev_list("STQ_Database", "giraph")
    valid_prs = validData_26("STQ_Database", "giraph")
    actual_xt, actual_yt, actual_zt = processing("STQ_Database", valid_prs, dev, rev, uq_map)
    assert actual_xt['fd3'] == 1.1686964596782044e-52
    assert actual_xt['fd5'] == 1.3077108315328655e-52
    assert actual_xt['fd1'] == 0
    assert actual_xt['fd4'] != 9.269031119592087e-221
    assert actual_yt[0] == 2.245988692891157e-85
    assert actual_yt[1] == 5.552321034881281e-85
    assert actual_yt[2] == 5.552321034881281e-85
    assert 5 not in actual_yt
    assert actual_zt['fd10'] == 5.716158155941897e-137
    assert actual_zt['fd11'] == 6.643155126566604e-137
    assert actual_zt['fd8'] == 0
    assert 'r-1' not in actual_zt

