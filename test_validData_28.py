from validData_28 import *

def test_validData_28():
    actual_output = validData_28("STQ_Database", "giraph")
    assert 'p1' in actual_output
    assert 'p2' not in actual_output
    assert 'p10' not in actual_output