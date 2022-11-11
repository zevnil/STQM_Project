from dev_rev_list import *
from validData_26 import *
from validData_27 import *
from validData_28 import *
from validData_29 import *
from validData_30 import *
from processing import *

dev, rev = dev_rev_list()
def q26(database, project):
    print('\n################################################                  26               ##############################################################')
    valid_prs = validData_26(database, project)
    Xt, Yt, Zt = processing(database, valid_prs, dev, rev)
    return Xt, Yt, Zt

def q27(database, project,module):
    print('\n#################################################                  27               ##############################################################')
    valid_prs = validData_27(database, project,module)
    Xt, Yt, Zt = processing(database, valid_prs, dev, rev)
    return Xt, Yt, Zt

def q28(database, project):
    print('\n#################################################                  28               ##############################################################')
    valid_prs = validData_28(database, project)
    Xt, Yt, Zt = processing(database, valid_prs, dev, rev)
    return Xt, Yt, Zt

def q29(database, project, module):
    print('\n#################################################                  29               ##############################################################')
    valid_prs = validData_29(database, project, module)
    Xt, Yt, Zt = processing(database, valid_prs, dev, rev)
    return Xt, Yt, Zt

def q30(database, project):
    print('\n#################################################                  30               ##############################################################')
    valid_prs = validData_30(database, project)
    Xt, Yt, Zt = processing(database, valid_prs, dev, rev)
    return Xt, Yt, Zt

q26("smartshark", "giraph")
q27("smartshark", "giraph", "giraph-core/src/main/java/org/apache/giraph/")
q28("smartshark", "giraph")
q29("smartshark", "giraph", "giraph-core/src/main/java/org/apache/giraph/")
q30("smartshark", "giraph")