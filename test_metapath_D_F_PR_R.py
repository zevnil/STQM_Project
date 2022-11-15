from metapath_D_F_PR_R import *
from dev_rev_list import *
from validData_26 import *

def test_metapath_D_F_PR_R():
    dev, rev = dev_rev_list("STQ", "giraph")
    valid_prs = validData_26("STQ", "giraph")
    actual_output = metapath_D_F_PR_R("STQ", valid_prs, dev, rev)
    assert actual_output[dev.index('d5')][rev.index('r4')] == 3
    assert actual_output[dev.index('d3')][rev.index('r3')] == 2
    assert actual_output[dev.index('d2')][rev.index('r1')] == 0
    assert actual_output[dev.index('d1')][rev.index('r3')] != 2