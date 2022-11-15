from validData_26 import *

def test_validData_26():
    actual_output = validData_26("STQ", "giraph")
    assert 'p4' in actual_output
    assert 'p6' in actual_output
    assert 'p2' not in actual_output
    assert 'p10' not in actual_output