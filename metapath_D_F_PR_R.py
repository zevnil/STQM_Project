from pymongo import MongoClient

def metapath_D_F_PR_R(pr_list, dev_list, rev_list):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request_data = db["pull_request"]
    pull_request_file = db["pull_request_file"]
    pull_request_review = db["pull_request_review"]

    t_f_i = {}

    pr_to_dev = {}
    t_pr_to_dev = {}
    for pr in pr_list:
        # print("For pr:", pr_list.index(pr))
        pr_to_dev[pr] = set()
        t_pr_to_dev[pr_list.index(pr)] = set()
        pr_details = pull_request_data.find({"_id": pr, "creator_id": {"$exists": True}})
        for d in pr_details:
            dev_id = d["creator_id"]
            # print("\t\t", dev_list.index(dev_id))
            pr_to_dev[pr].add(dev_id)
            t_pr_to_dev[pr_list.index(pr)].add(dev_list.index(dev_id))
    
    print("t_pr_to_dev:")
    for k in t_pr_to_dev:
        print("KEY:", k)
        print("VALUE:", t_pr_to_dev.get(k))

    dev_to_file = {}
    file_to_pr = {}
    t_dev_to_file = {}
    t_file_to_pr = {}
    for pr in pr_list:
        pr_file_details = pull_request_file.find({"pull_request_id": pr, "path": {"$exists": True}})
        for d in pr_file_details:
            f = d["path"]

            if f not in t_f_i:
                t_f_i[f] = len(t_f_i)

            if f not in file_to_pr:
                file_to_pr[f] = set()
            file_to_pr[f].add(pr)

            if t_f_i[f] not in t_file_to_pr:
                t_file_to_pr[t_f_i[f]] = set()
            t_file_to_pr[t_f_i[f]].add(pr_list.index(pr))

            for dev in pr_to_dev.get(pr):
                if dev not in dev_to_file:
                    dev_to_file[dev] = set()
                dev_to_file[dev].add(f)

                if dev_list.index(dev) not in t_dev_to_file:
                    t_dev_to_file[dev_list.index(dev)] = set()
                t_dev_to_file[dev_list.index(dev)].add(t_f_i[f])
    
    print("\n\nt_dev_to_file:")
    for k in t_dev_to_file:
        print("KEY:", k)
        print("VALUE:", t_dev_to_file.get(k))
    
    print("\n\nt_file_to_pr:")
    for k in t_file_to_pr:
        print("KEY:", k)
        print("VALUE:", t_file_to_pr.get(k))
    
    pr_to_rev = {}
    t_pr_to_rev = {}
    for pr in pr_list:
        pr_to_rev[pr] = set()
        t_pr_to_rev[pr_list.index(pr)] = set()
        pr_rev_details = pull_request_review.find({"pull_request_id": pr, "creator_id": {"$exists": True}})
        for d in pr_rev_details:
            rev_id = d["creator_id"]

            pr_to_rev[pr].add(rev_id)
            t_pr_to_rev[pr_list.index(pr)].add(rev_list.index(rev_id))
    
    print("\n\nt_pr_to_rev:")
    for k in t_pr_to_rev:
        print("KEY:", k)
        print("VALUE:", t_pr_to_rev.get(k))

    print("No. of Dev:", len(dev_list))
    print("No. of Rev:", len(rev_list))
    print("No. of PRs:", len(pr_list))
    print("No. of Files:", len(t_f_i))

    print("\nFILES:")
    for f in t_f_i:
        print(f)

    num_rows = len(dev_list)
    num_cols = len(rev_list)
    ret_matrix = [[0]*num_cols]*num_rows

    for dev in dev_list:
        if dev in dev_to_file:
            for f in dev_to_file.get(dev):
                if f in file_to_pr:
                    for pr in file_to_pr.get(f):
                        if pr in pr_to_rev:
                            for rev in pr_to_rev.get(pr):
                                ret_matrix[dev_list.index(dev)][rev_list.index(rev)] += 1
    
    print("\nD_F_PR_R matrix:")
    for i in range(num_rows):
        print(ret_matrix[i])
    
    return ret_matrix