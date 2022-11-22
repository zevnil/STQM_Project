from metapath_D_F_PR_R import *
from dev_rev_list import *
from validData_26 import *

def test_metapath_D_F_PR_R():
    dev, rev, uq_map = dev_rev_list("STQ_Database", "giraph")
    valid_prs = validData_26("STQ_Database", "giraph")
    actual_output = metapath_D_F_PR_R("STQ_Database", valid_prs, dev, rev, uq_map)
    assert actual_output[dev.index('fd5')][rev.index('fd11')] == 3
    assert actual_output[dev.index('fd3')][rev.index('fd10')] == 2
    assert actual_output[dev.index('fd2')][rev.index('fd8')] == 0
    assert actual_output[dev.index('fd1')][rev.index('fd10')] != 2
