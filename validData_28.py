from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["smartshark"]
pull_request_data = db["pull_request"]
review_data = db["pull_request_review"]
pull_request_system = db["pull_request_system"]
project_id = db["project"].find({"name": "giraph"})
p_id = project_id[0]['_id']

def validData_28():
    mean_review_time = 0
    count_review_time = 0
    pr_details = []
    valid_pr = []
    # dev = []
    # rev = []

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
                pr_details = [[pull_request_id, (approved_time - submitted_time).total_seconds(), dev_id, rev_id]]
            else:
                pr_details.append([pull_request_id,(approved_time - submitted_time).total_seconds(), dev_id, rev_id])

    if count_review_time == 0:
        return {-1}, {-1}, {-1} 
    print("Sum:", mean_review_time)
    print("Count:", count_review_time)
    mean_review_time = mean_review_time / count_review_time
    print("Mean review time: ", mean_review_time)

    for item in pr_details:
        if item[1] > mean_review_time:
            valid_pr.append(item[0])
            # if item[2] not in dev:
            #     dev.append(item[2])
            # if item[3] not in rev:
            #     rev.append(item[3])

    # pull_request_comments = review_data.find({"state": "COMMENTED", "creator_id": {"$exists": True}})
    # for item in pull_request_comments:
    #     if item["pull_request_id"] in valid_pr and item["creator_id"] not in rev:
    #         rev.append(item["creator_id"])

    print("VALID PRS: ")
    print(valid_pr)
    # print("DEV IDS:")
    # print(dev)
    # print("REV IDS: ")
    # print(rev)
    
    return valid_pr