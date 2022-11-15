import metapath_D_PR_F_PR_R
import validData_26
from dev_rev_list import *

def test_D_PR_F_PR_R():
    dev_list,rev_list=dev_rev_list("STQ","giraph")
    pr_list=validData_26.validData_26("STQ","giraph")


    mat_p3=metapath_D_PR_F_PR_R.metapath_D_PR_F_PR_R("STQ",pr_list,dev_list,rev_list)

    assert(mat_p3[dev_list.index('d1')][rev_list.index('r3')])==0
    assert(mat_p3[dev_list.index('d3')][rev_list.index('r3')])==2
    assert(mat_p3[dev_list.index('d5')][rev_list.index('r4')])==3