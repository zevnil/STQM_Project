from dev_rev_list import *
from validData_26 import *
from validData_27 import *
from validData_28 import *
from validData_29 import *
from validData_30 import *
from processing import *

dev, rev = dev_rev_list()
def q26():
    print('\n################################################                  26               ##############################################################')
    valid_prs = validData_26()
    Xt, Yt, Zt = processing(valid_prs, dev, rev)
    return Xt, Yt, Zt

def q27(module):
    print('\n#################################################                  27               ##############################################################')
    valid_prs = validData_27(module)
    Xt, Yt, Zt = processing(valid_prs, dev, rev)
    return Xt, Yt, Zt

def q28():
    print('\n#################################################                  28               ##############################################################')
    valid_prs = validData_28()
    Xt, Yt, Zt = processing(valid_prs, dev, rev)
    return Xt, Yt, Zt

def q29(module):
    print('\n#################################################                  29               ##############################################################')
    valid_prs = validData_29(module)
    Xt, Yt, Zt = processing(valid_prs, dev, rev)
    return Xt, Yt, Zt

def q30():
    print('\n#################################################                  30               ##############################################################')
    valid_prs = validData_28()
    Xt, Yt, Zt = processing(valid_prs, dev, rev)
    return Xt, Yt, Zt

q26()
q27("giraph-core/src/main/java/org/apache/giraph/")
q28()
q29("giraph-core/src/main/java/org/apache/giraph/")
q30()