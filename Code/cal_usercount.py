import json
import os
import pandas as pd


def cal_appeartime(filenames):
    for filename in filenames:
        group = filename.split('.')[0]
        df = pd.DataFrame(pd.read_excel(filename))
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


if __name__ == "__main__":
    cases = {}
    usercount = {"group1": 55,
                 "group2": 55,
                 "group3": 55,
                 "group4": 49,
                 "group5": 41}
    os.chdir(os.getcwd() + "//Groups")
    cal_appeartime(os.listdir())
    save_as_file(cases, "../Data/grouping.json")

    with open("test_data.json", encoding='utf-8') as f:
        data = json.loads(f.read())


