from pymongo import MongoClient

def metapath_D_PR_R(pr_list, dev_list, rev_list):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request_data = db["pull_request"]
    pull_request_review_data = db["pull_request_review"]

    for pr in pr_list:
        dev_list=pull_request_data.find({"_id":pr['_id']})
        rev_list=pull_request_review_data.find({"pull_request_id":pr['_id']})
        

    num_rows = len(dev_list)
    num_cols = len(rev_list)
    ret_matrix = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for dev in dev_list:
        dev_i = dev['creator_id']
        pull_request_list = pull_request_data.find({"_creator_id": dev})
        #pr_id=pull_request_list['pull_request_id']
        for pd in pull_request_list:
            rev_list=pull_request_review_data.find({"pull_request_id":pd['pull_request_id']})
            for rev in rev_list:
                rev_i = rev['creator_id']
                ret_matrix[dev_list.index(dev_i)][rev_list.index(rev_i)] += 1
    
    print("\nD_PR_R matrix:")
    for i in range(num_rows):
        print(ret_matrix[i])
    
    return ret_matrix


