from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["smartshark"]
pull_request_data = db["pull_request"]
review_data = db["pull_request_review"]
pull_request_system = db["pull_request_system"]
pull_request_file=db['pull_request_file']
file=db['file']

def metapath_D_PR_F_PR_R(pr_list):
    mean_review_time = 0
    count_review_time = 0
    pr_details = []
    valid_pr = []
    dev_set = set()
    rev_set = set()
    for pr in pr_list:
        # got the list of developers who have created prs with pr_id = pr ki id 
        dev_list=pull_request_data.find({"_id":pr['_id']})
        # list of file paths which have been changed by pr_id
        file_path=pull_request_file.find({"pull_request_id": pr['_id']})
        for fp in file_path:
            fpath = fp['path']
            #now since we have got the path we will extract the id from file collection using this path
            file_details= file.find({"path":fpath})
            file_id=file_details[0]['_id']

            #f->pr
            pr_details=pull_request_file.find({"path":fpath})
            #pr_id=pr_details['pull_request_id']
            for pd in pr_details:
                rev_list=review_data.find({"pull_request_id":pd['pull_request_id']})

    for dev in dev_list:
        pull_request_list = pull_request_data.find({"_creator_id": dev})
        for pr in pull_request_list:
            file_path=pull_request_file.find({"pull_request_id": pr['_id']})
            for fp in file_path:
                fpath = fp['path']
                #now since we have got the path we will extract the id from file collection using this path
                file_details= file.find({"path":fpath})
                file_id=file_details[0]['_id']

                #f->pr
                pr_details=pull_request_file.find({"path":fpath})
                #pr_id=pr_details['pull_request_id']
                for pd in pr_details:
                    rev_list=review_data.find({"pull_request_id":pd['pull_request_id']})
                    cnt+=1


# it contains all those prs which have been approved 
# it will create developer reviewer pair
    #pull_request_ids = review_data.find({"state": "APPROVED", "creator_id": {"$exists": True}, "submitted_at": {"$exists": True}})

    # in pull_request_file table we have the file paths which have been changed by a particular pr
    # in file we have file id and the file paths 
    # so if we do one to one mapping b/w file paths in both we can map pr_id to file_id




    num_rows = len(dev_list)
    num_cols = len(rev_list)
    ret_matrix = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for dev in dev_list:
        dev_i = dev['creator_id']
        pull_request_list = pull_request_data.find({"_creator_id": dev})
        for pr in pull_request_list:
            file_path=pull_request_file.find({"pull_request_id": pr['_id']})
            for fp in file_path:
                fpath = fp['path']
                #now since we have got the path we will extract the id from file collection using this path
                file_details= file.find({"path":fpath})
                file_id=file_details[0]['_id']

                #f->pr
                pr_details=pull_request_file.find({"path":fpath})
                #pr_id=pr_details['pull_request_id']
                for pd in pr_details:
                    rev_list=review_data.find({"pull_request_id":pd['pull_request_id']})
                    for rev in rev_list:
                        rev_i = rev['creator_id']
                        ret_matrix[dev_list.index(dev_i)][rev_list.index(rev_i)] += 1
                    


    for i in ret_matrix:
        for j in ret_matrix[i]:
            print(j)
            print('/n')

    return ret_matrix