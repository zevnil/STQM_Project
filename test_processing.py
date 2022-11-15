from processing import *
from dev_rev_list import *
from validData_26 import *

def test_processing():
    dev, rev = dev_rev_list("STQ", "giraph")
    valid_prs = validData_26("STQ", "giraph")
    actual_xt, actual_yt, actual_zt = processing("STQ", valid_prs, dev, rev)
    assert actual_xt['d3'] == 1.1686964596782044e-52
    assert actual_xt['d5'] == 1.3077108315328655e-52
    assert actual_xt['d1'] == 0
    assert actual_xt['d4'] != 9.269031119592087e-221
    assert actual_yt[0] == 2.245988692891157e-85
    assert actual_yt[1] == 5.552321034881281e-85
    assert actual_yt[2] == 5.552321034881281e-85
    assert 5 not in actual_yt
    assert actual_zt['r3'] == 5.716158155941897e-137
    assert actual_zt['r4'] == 6.643155126566604e-137
    assert actual_zt['r1'] == 0
    assert 'r-1' not in actual_zt

