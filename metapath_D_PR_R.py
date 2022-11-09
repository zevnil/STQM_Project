from pymongo import MongoClient

def metapath_D_PR_R(pr_list, dev_list, rev_list):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request_data = db["pull_request"]
    pull_request_review_data = db["pull_request_review"]

    pr_to_dev = {}
    # pr_to_dev = {}
    for pr in pr_list:
        pr_to_dev[pr] = set()
        # pr_to_dev[pr_list.index(pr)] = set()
        pr_dev_details = pull_request_data.find({"_id": pr, "creator_id": {"$exists": True}})
        for d in pr_dev_details:
            dev_id = d["creator_id"]
            pr_to_dev[pr].add(dev_id)
            # pr_to_dev[pr_list.index(pr)].add(dev_list.index(dev_id))

    dev_to_pr = {}
    # dev_to_pr = {}
    for dev in dev_list:
        dev_to_pr[dev] = set()

        pr_dev_details = pull_request_data.find({"creator_id": dev, "_id": {"$exists": True}})
        for pr in pr_dev_details:
            pr_id = pr["_id"]
            dev_to_pr[dev].add(pr_id)
            # dev_to_pr[dev_list.index(dev)].add(pr_list.index(pr_id))

    pr_to_rev = {}
    # pr_to_rev = {}
    for pr in pr_list:
        pr_to_rev[pr] = set()
        # pr_to_rev[pr_list.index(pr)] = set()
        pr_rev_details = pull_request_review_data.find({"pull_request_id": pr, "creator_id": {"$exists": True}})
        for d in pr_rev_details:
            rev_id = d["creator_id"]
            pr_to_rev[pr].add(rev_id)
            # pr_to_rev[pr_list.index(pr)].add(rev_list.index(rev_id))

    num_rows = len(dev_list)
    num_cols = len(rev_list)
    ret_matrix = [[0 for i in range(num_cols)] for j in range(num_rows)]
    
    for dev in dev_list:
        if dev in dev_to_pr:
            for pr in dev_to_pr.get(dev):
                if pr in pr_to_rev:
                    for rev in pr_to_rev.get(pr):
                        ret_matrix[dev_list.index(dev)][rev_list.index(rev)] += 1
    
    print("\nD_PR_R matrix:")
    for i in range(num_rows):
        print(ret_matrix[i])
    
    return ret_matrix


