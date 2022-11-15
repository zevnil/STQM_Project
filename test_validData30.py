import validData_30

def test_validData30():
    actual_output=validData_30.validData_30("STQ","giraph")
    assert "p4" in actual_output
    assert "p3" not in actual_output
    assert "p10" not in actual_output
    assert "p6" in actual_output
    assert "p-1" not in actual_output
