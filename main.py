from validData_26 import *
from metapath_D_PR_R import *
from metapath_D_F_PR_R import *
from metapath_D_PR_F_PR_R import *
from processing import *

valid_prs, dev, rev = validData()
D_PR_R_matrix = metapath_D_PR_R(valid_prs, dev, rev)
D_F_PR_R_matrix = metapath_D_F_PR_R(valid_prs, dev, rev)
D_PR_F_PR_R_matrix = metapath_D_PR_F_PR_R(valid_prs, dev, rev)
processing(D_PR_R_matrix, D_F_PR_R_matrix, D_PR_F_PR_R_matrix, dev, rev)