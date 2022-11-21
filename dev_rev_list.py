from pymongo import MongoClient
from datetime import datetime

def dev_rev_list(database, project):
    dev_set = set()
    rev_set = set()
    uq_map = {}

    client = MongoClient("mongodb://localhost:27017/")
    db = client[database]
    pull_request_data = db["pull_request"]
    review_data = db["pull_request_review"]
    final_identity = db["final_identity"]
    pull_request_system = db["pull_request_system"]
    people_data = db["people"]
    project_id = db["project"].find({"name": project})
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
            if dev_id not in uq_map:
                # print(1)
                uq_id = list(final_identity.find({"people": dev_id}))
                # print(uq_id[0]["_id"])
                for uq in uq_id:
                    # print(1)
                    uq_map[dev_id] = uq["_id"]
            if rev_id not in uq_map:
                uq_id = final_identity.find({"people": rev_id})
                for uq in uq_id:
                    uq_map[rev_id] = uq["_id"]
            # print(uq_map)
            dev_set.add(uq_map[dev_id])
            rev_set.add(uq_map[rev_id])

    return list(dev_set), list(rev_set), uq_map