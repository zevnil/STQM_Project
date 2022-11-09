from pymongo import MongoClient

def metapath_D_PR_F_PR_R(pr_list, dev_list, rev_list):

    client = MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request_data = db["pull_request"]
    pull_request_review = db["pull_request_review"]
    pull_request_file=db['pull_request_file']
    file=db['file']

    pr_to_dev = {}
    # t_pr_to_dev = {}
    for pr in pr_list:
        pr_to_dev[pr] = set()
        # t_pr_to_dev[pr_list.index(pr)] = set()
        pr_details = pull_request_data.find({"_id": pr, "creator_id": {"$exists": True}})
        for d in pr_details:
            dev_id = d["creator_id"]
            pr_to_dev[pr].add(dev_id)
            # t_pr_to_dev[pr_list.index(pr)].add(dev_list.index(dev_id))

    dev_to_pr = {}
    # dev_to_pr = {}
    for dev in dev_list:
        dev_to_pr[dev] = set()

        pr_dev_details = pull_request_data.find({"creator_id": dev, "_id": {"$exists": True}})
        for pr in pr_dev_details:
            pr_id = pr["_id"]
            dev_to_pr[dev].add(pr_id)
            # dev_to_pr[dev_list.index(dev)].add(pr_list.index(pr_id))
    
    pr_to_file = {}
    # t_pr_to_file = {}
    for pr in pr_list:
        pr_to_file[pr] = set()
        pr_file_details = pull_request_file.find({"pull_request_id": pr, "path": {"$exists": True}})
        for d in pr_file_details:
            file_path = d["path"]
            file_details = file.find({"path": file_path, "_id" : True})
            for fd in file_details:
                f = fd["_id"]
                pr_to_file[pr].add(f)

    file_to_pr = {}
    # t_file_to_pr = {}
    for pr in pr_list:
        pr_file_details = pull_request_file.find({"pull_request_id": pr, "path": {"$exists": True}})
        for d in pr_file_details:
            f = d["path"]

            # if f not in t_f_i:
            #     t_f_i[f] = len(t_f_i)

            if f not in file_to_pr:
                file_to_pr[f] = set()
            file_to_pr[f].add(pr)

    # print("\n\nt_file_to_pr:")
    # for k in t_file_to_pr:
    #     print("KEY:", k)
    #     print("VALUE:", t_file_to_pr.get(k))
    
    pr_to_rev = {}
    # t_pr_to_rev = {}
    for pr in pr_list:
        pr_to_rev[pr] = set()
        # t_pr_to_rev[pr_list.index(pr)] = set()
        pr_rev_details = pull_request_review.find({"pull_request_id": pr, "creator_id": {"$exists": True}})
        for d in pr_rev_details:
            rev_id = d["creator_id"]

            pr_to_rev[pr].add(rev_id)
            # t_pr_to_rev[pr_list.index(pr)].add(rev_list.index(rev_id))
    

    num_rows = len(dev_list)
    num_cols = len(rev_list)
    ret_matrix = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for dev in dev_list:
        # print("DEVELOPER: ", dev)
        if dev in dev_to_pr:
            for _pr in dev_to_pr.get(dev):
                if _pr in pr_to_file:
                    for f in pr_to_file.get(_pr):
                        if f in file_to_pr:
                            for pr in file_to_pr.get(f):
                                if pr in pr_to_rev:
                                    for rev in pr_to_rev.get(pr):
                                        # print("REVIEWER: ", rev)
                                        ret_matrix[dev_list.index(dev)][rev_list.index(rev)] += 1
    
    print("\nD_PR_ F_PR_R matrix:")
    for i in range(num_rows):
        print(ret_matrix[i])
    
    return ret_matrix
