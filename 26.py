from pymongo import MongoClient
from metapath_D_F_PR_R import *
from metapath_D_PR_R import *
from metapath_D_PR_F_PR_R import *

import sys
sys.stdout = open('ishneet_output.txt','wt')

client = MongoClient("mongodb://localhost:27017/")
db = client["smartshark"]
pull_request_data = db["pull_request"]
review_data = db["pull_request_review"]
pull_request_system = db["pull_request_system"]
project_id = db["project"].find({"name": "giraph"})
p_id = project_id[0]['_id']
P = {'D_PR_R' : 1, 'D_PR_F_PR_R' : 2}
D_R_P = {}
D_R = {}
R_P = {}
D_P = {}

def validPRs():
    mean_review_time = 0
    count_review_time = 0
    pr_details = []
    valid_pr = []
    dev_set = set()
    rev_set = set()

    pull_request_ids = review_data.find({"state": "APPROVED", "creator_id": {"$exists": True}, "submitted_at": {"$exists": True}})
    for pr_id in pull_request_ids:
        rev_id = pr_id["creator_id"]
        approved_time = pr_id["submitted_at"]
        pull_request_id = pr_id["pull_request_id"]
        pull_request = pull_request_data.find({"_id": pull_request_id, "creator_id": {"$exists": True}, "created_at": {"$exists": True}})
        
        for pr in pull_request:
            pr_system = pull_request_system.find({"_id": pr["pull_request_system_id"]})
            if pr_system[0]["project_id"] != p_id:
                continue
            dev_id = pr["creator_id"]
            submitted_time = pr["created_at"]
            mean_review_time += (approved_time - submitted_time).total_seconds()
            count_review_time += 1
            if len(pr_details) == 0:
                pr_details = [[pull_request_id, (approved_time - submitted_time).total_seconds()]]
            else:
                pr_details.append([pull_request_id,(approved_time - submitted_time).total_seconds()])
            
            dev_set.add(dev_id)
            rev_set.add(rev_id)

    
    print("Sum:", mean_review_time)
    print("Count:", count_review_time)
    mean_review_time = mean_review_time / count_review_time
    print("Mean review time: ", mean_review_time)

    for item in pr_details:
        if item[1] <= mean_review_time:
            valid_pr.append(item[0])
    return valid_pr, list(dev_set), list(rev_set)
    # return valid_pr


# I REMEMBER SIR NE EK BAAR BOLA THA KI SAARE DEVELOPERS AND REVIEWERS HONE CHAAHIYE RANK MEIN... 
# EVEN IF THEY GET 0 AS SCORE (I.E., KAHIN KISI PATH MEIN NA AAYEIN)
# BUT THIS FUNCTION IS TAKING SUFFICIENTLY LONG, AND MAY STILL GIVE INCOMPLETE LISTS...

def dev_rev_list():
    dev_set = set()
    rev_set = set()

    pull_request_ids = review_data.find({"creator_id": {"$exists": True}})
    for pr_id in pull_request_ids:
        rev_id = pr_id["creator_id"]
        pull_request_id = pr_id["pull_request_id"]
        pull_request = pull_request_data.find({"_id": pull_request_id, "creator_id": {"$exists": True}})
        
        for pr in pull_request:
            pr_system = pull_request_system.find({"_id": pr["pull_request_system_id"]})
            if pr_system[0]["project_id"] != p_id:
                continue
            dev_id = pr["creator_id"]
            
            dev_set.add(dev_id)
            rev_set.add(rev_id)
    
    return list(dev_set), list(rev_set)

# def D_PR_R(valid_pr):
#     dev_count = {}
#     rev_count = {}
#     dev_u_rev_count = {}
#     for item in pr_details:
#         if(item[1] < mean_review_time):
#             d = item[2]
#             r = item[3]
#             if d in dev_count:
#                 temp = dev_count.get(d)
#                 dev_count[d] = temp+1
#             else:
#                 dev_count[d] = 1

#             if r in rev_count:
#                 temp = rev_count.get(r)
#                 rev_count[r] = temp+1
#             else:
#                 rev_count[r] = 1
            
#             t = (d, r)
#             if t in dev_u_rev_count:
#                 temp = dev_u_rev_count.get(t)
#                 temp = temp+1
#                 dev_u_rev_count[t] = temp
#             else:
#                 dev_u_rev_count[t] = 1
    
#     D0 = {}
#     R0 = {}
#     # P0 = {}

#     for d in dev_count:
#         D0[d] = 1/len(dev_count)
#         # print(D0[d])
    
#     # print("\n\n")
#     for r in rev_count:
#         R0[r] = 1/len(rev_count)
#         # print(R0[r])
    
#     # P0["path 1"] = 1 / 1
    
#     # d0 = 1 / len(dev_count)
#     # r0 = 1 / len(rev_count)
#     p0 = 1

#     for i in range(5):
#         for d in D0:
#             dt = 0

#             for r in R0:
#                 # print(dev_u_rev_count.get((d, r)))
#                 # print(rev_count.get(r))
#                 # print()
#                 if (d, r) not in dev_u_rev_count:
#                     continue
#                 dt += dev_u_rev_count.get((d, r)) / rev_count.get(r) * R0[r] * p0
#                 # for p in P0:
#                 #     dt += dev_u_rev_count.get((d, r)) / rev_count.get(r) * R0[r] * P0[p]
            
#             D0[d] = dt
    
#         pt = 0
#         for d in D0:
#             for r in R0:
#                 if (d, r) not in dev_u_rev_count:
#                     continue
#                 pt += 1 * D0[d] * R0[r]
#         p0 = pt

#         for r in R0:
#             rt = 0

#             for d in D0:
#                 if (d, r) not in dev_u_rev_count:
#                     continue
#                 rt += dev_u_rev_count.get((d, r)) / dev_count.get(d) * D0[d] * p0
            
#             R0[r] = rt
        
#         # print(i)
#         # print("D0 : ")
#         # print(D0, "\n\n")
#         # print("R0 : ")
#         # print(R0, "\n\n")
#         # print("p0 = ", p0)
    
#     print("p0 = ", p0)

#     dev_tup_list = []
#     rev_tup_list = []

#     for k in D0:
#         v = D0.get(k)
#         if len(dev_tup_list) == 0:
#             dev_tup_list = [(v, k)]
#         else:
#             dev_tup_list.append((v, k))

#     for k in R0:
#         v = R0.get(k)
#         if len(rev_tup_list) == 0:
#             rev_tup_list = [(v, k)]
#         else:
#             rev_tup_list.append((v, k))
    
#     dev_tup_list.sort(key = lambda x : x[0], reverse = True)
#     print("Developer ranks:")
#     print("Developer\t-\td0 Score")
#     for s in dev_tup_list:
#         print(s[1], "\t-\t", s[0])
#     # print(dev_tup_list)
#     print("\n\n")
#     rev_tup_list.sort(key = lambda x : x[0], reverse = True)
#     print("Reviewer ranks:")
#     print("Reviewer\t-\tr0 Score")
#     for s in rev_tup_list:
#         print(s[1], "\t-\t", s[0])
#     # print(rev_tup_list)
#     print("\n\n")

prs, dev_list, rev_list = validPRs()
# prs = validPRs()
print("VALID PRs:")
print(prs, "\n\n")

# dev_list, rev_list = dev_rev_list()
print("DEVELOPER LIST:")
print(dev_list, "\n\n")
print("REVIEWER LIST:")
print(rev_list, "\n\n")

# rt_mat = metapath_D_PR_R(prs, dev_list, rev_list)
# rt_mat = metapath_D_F_PR_R(prs, dev_list, rev_list)
rt_mat = metapath_D_PR_F_PR_R(prs, dev_list, rev_list)