import metapath_D_PR_F_PR_R
import validData_26
from dev_rev_list import *

def test_D_PR_F_PR_R():
    dev_list,rev_list, uq_map=dev_rev_list("STQ_Database","giraph")
    pr_list=validData_26.validData_26("STQ_Database","giraph")


    mat_p3=metapath_D_PR_F_PR_R.metapath_D_PR_F_PR_R("STQ_Database",pr_list,dev_list,rev_list, uq_map)

    assert(mat_p3[dev_list.index('fd1')][rev_list.index('fd10')])==0
    assert(mat_p3[dev_list.index('fd3')][rev_list.index('fd10')])==2
    assert(mat_p3[dev_list.index('fd5')][rev_list.index('fd11')])==3