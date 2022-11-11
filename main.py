from dev_rev_list import *
from validData_26 import *
from validData_27 import *
from validData_28 import *
from validData_29 import *
from validData_30 import *
from processing import *

dev, rev = dev_rev_list()
print('\n################################################                  26               ##############################################################')
valid_prs = validData_26()
processing(valid_prs, dev, rev)

print('\n#################################################                  27               ##############################################################')
valid_prs = validData_27()
processing(valid_prs, dev, rev)

print('\n#################################################                  28               ##############################################################')
valid_prs = validData_28()
processing(valid_prs, dev, rev)

print('\n#################################################                  29               ##############################################################')
valid_prs = validData_29()
processing(valid_prs, dev, rev)

print('\n#################################################                  30               ##############################################################')
valid_prs = validData_30()
processing(valid_prs, dev, rev)
