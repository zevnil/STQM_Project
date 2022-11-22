import validData_29
from dev_rev_list import dev_rev_list
from metapath_D_F_PR_R import metapath_D_F_PR_R
from validData_26 import validData_26

def test_validData29():
    actual_output=validData_29.validData_29("STQ_Database","giraph","a/b/c")
    assert "p1" in actual_output
    assert "p3" not in actual_output
    assert "p10" not in actual_output
    assert "p-1" not in actual_output



