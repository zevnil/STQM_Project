import dev_rev_list

pres_dev = ["fd1", "fd2", "fd3", "fd4", "fd5"]
abs_dev = ["fd6", "fd7"]

pres_rev = ["fd8", "fd9", "fd10", "fd11"]
abs_rev = ["fd14"]

abs_key_uq = ["d6", "d7", "r5", "r6", "r7"]
pres_key_uq = ["d1", "d2", "d3", "d4", "d5", "r1", "r2", "r3", "r4"]
pres_value_uq = ["fd1", "fd2", "fd3", "fd4", "fd5", "fd8", "fd9", "fd10", "fd11"]

def test_dev_rev_list():
    dev_list, rev_list, uq_map = dev_rev_list.dev_rev_list("STQ_Database", "giraph")

    for dev in pres_dev:
        assert dev in dev_list
    
    for dev in abs_dev:
        assert dev not in dev_list

    for rev in pres_rev:
        assert rev in rev_list
    
    for rev in abs_rev:
        assert rev not in rev_list

    for k in abs_key_uq:
        assert k not in uq_map
    
    for i in range(len(pres_key_uq)):
        assert uq_map[pres_key_uq[i]] == pres_value_uq[i]
