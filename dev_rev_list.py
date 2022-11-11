from pymongo import MongoClient
from datetime import datetime

def dev_rev_list():
    dev_set = set()
    rev_set = set()

    client = MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request_data = db["pull_request"]
    review_data = db["pull_request_review"]
    pull_request_system = db["pull_request_system"]
    project_id = db["project"].find({"name": "giraph"})
    p_id = project_id[0]['_id']

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