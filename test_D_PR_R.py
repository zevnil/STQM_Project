import metapath_D_PR_R
from dev_rev_list import *
import validData_26

def test_metapath_D_PR_R():

    dev_list, rev_list, uq_map = dev_rev_list("STQ_Database","giraph")
    pr_list = validData_26.validData_26("STQ_Database", "giraph")

    matrix_D_PR_R = metapath_D_PR_R.metapath_D_PR_R("STQ_Database", pr_list, dev_list, rev_list, uq_map)

    assert (matrix_D_PR_R[dev_list.index("fd4")][rev_list.index("fd11")]) ==0
    assert (matrix_D_PR_R[dev_list.index("fd3")][rev_list.index("fd10")]) ==1
    assert (matrix_D_PR_R[dev_list.index("fd5")][rev_list.index("fd11")]) ==1