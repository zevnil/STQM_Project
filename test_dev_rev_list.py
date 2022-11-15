import dev_rev_list

pres_dev = ["d1", "d2", "d3", "d4", "d5"]
abs_dev = ["d6", "d7"]

pres_rev = ["r1", "r2", "r3", "r4"]
abs_rev = ["r7"]

def test_dev_rev_list():
    dev_list, rev_list = dev_rev_list.dev_rev_list("STQ", "giraph")

    for dev in pres_dev:
        assert dev in dev_list
    
    for dev in abs_dev:
        assert dev not in dev_list

    for rev in pres_rev:
        assert rev in rev_list
    
    for rev in abs_rev:
        assert rev not in rev_list
