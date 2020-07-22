"""
计算每组人数和对应题目
"""

import json
import os
import pandas as pd
import difflib


def cal_appeartime(filenames):
    for filename in filenames:
        group = filename.split('.')[0]
        df = pd.DataFrame(pd.read_excel(filename))
        grouping[group] = sorted(list(df["id"]))
        for row in df.itertuples():
            case_id, difficulty = getattr(row, "id"), getattr(row, "difficulty")
            if case_id not in cases.keys():
                cases[case_id] = {"group": [group],
                                  "difficulty": difficulty,
                                  "planed_usercount":usercount[group]}
            else:
                cases[case_id]["group"].append(group)
                cases[case_id]["planed_usercount"] += usercount[group]


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def infer_group(data:dict):
    grouping_users = {}
    for user_id, details in data.items():
        if len(details["cases"]) > 10:
            user_case_ids = sorted([int(case["case_id"]) for case in details["cases"]])
            most_similar = ""
            max_ratio = 0
            for group, group_case_ids in grouping.items():
                '''
                ratio = difflib.SequenceMatcher(None, user_case_ids, group_case_ids).quick_ratio()
                if ratio > max_ratio:
                    most_similar = group
                    max_ratio = ratio
                '''
                if set(user_case_ids) <= set(group_case_ids):
                    most_similar = group
            if most_similar == "":
                print(user_id, user_case_ids)
            details["group"] = most_similar

            if most_similar in grouping_users.keys():
                grouping_users[most_similar].append(user_id)
            else:
                grouping_users[most_similar] = [user_id]

    for groupname, users in grouping_users.items():
        print(groupname + "  usercount: " + str(len(users)))
    return grouping_users

if __name__ == "__main__":
    cases = {}
    grouping = {}
    usercount = {"group1": 47,
                 "group2": 50,
                 "group3": 52,
                 "group4": 43,
                 "group5": 62
                 }
    backpath = os.getcwd()
    os.chdir(os.getcwd() + "//Groups")
    cal_appeartime(os.listdir())

    os.chdir(backpath)
    # save_as_file(cases, "../Data/new_cases_information.json")
    save_as_file(grouping, "../Data/grouping_cases.json")

    with open('../Data/newtest_data.json', encoding='utf-8') as f:
        data = json.loads(f.read())
    infer_group(data)
    save_as_file(infer_group(data), "../Data/grouping_users.json")


'''
group1  usercount: 47
group2  usercount: 49+1
group3  usercount: 51+1
group4  usercount: 43
group5  usercount: 62
'''


