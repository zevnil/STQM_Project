import metapath_D_PR_R
from dev_rev_list import *
import validData_26

def test_metapath_D_PR_R():

    dev_list, rev_list = dev_rev_list("STQ","giraph")
    pr_list = validData_26.validData_26("STQ", "giraph")

    matrix_D_PR_R = metapath_D_PR_R.metapath_D_PR_R("STQ", pr_list, dev_list, rev_list)

    assert (matrix_D_PR_R[dev_list.index("d4")][rev_list.index("r4")]) ==0
    assert (matrix_D_PR_R[dev_list.index("d3")][rev_list.index("r3")]) ==1
    assert (matrix_D_PR_R[dev_list.index("d5")][rev_list.index("r4")]) ==1