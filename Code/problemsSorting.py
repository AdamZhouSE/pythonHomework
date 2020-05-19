import json
import numpy as np
import pandas as pd
import cal_num_of_line as cl

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def sorting(data: list):
    problems = {}
    count = 0
    for user_id, details in data.items():
        cases = details['cases']
        for case in cases:
            if case["case_id"] not in problems.keys():
                problems[case["case_id"]] = {"case_id": case['case_id'],
                                             "case_type": case["case_type"],
                                             "case_zip": case["case_zip"],
                                             "records": []
                                             }
            problems[case["case_id"]]["records"].append({"user_id": user_id,
                                                         "final_score": case["final_score"],
                                                         "upload_times": len(case["upload_records"]),
                                                         "upload_records": case["upload_records"]
                                                         })
        count += 1
        print(count, 'has done')
    return analyse(problems)


def save_as_file(data: list, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def analyse(data: list):
    for case_id, details in data.items():
        records = details["records"]
        data[case_id]["total_upload_times"] = sum([record["upload_times"] for record in records])
        data[case_id]["average_score"] = sum([record["final_score"] for record in records]) / len(records)
        data[case_id]["user_count"] = len(records)

        for record in records:
            user_id = record["user_id"]
            for up in record["upload_records"]:
                upload_id = str(up["upload_id"])
                filepath = 'Code_Records//' + case_id + "//" + user_id + "//" + upload_id + "//" + "answer.py"
                try:
                    lst = cl.calc_line_num(filepath)
                    up["num_of_line"] = lst[0]
                except:
                    continue
    return data

if __name__ == '__main__':
    f = open('data/test_data.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    save_as_file(sorting(data), 'data/Database of Mooctest.json')

    f = open('data/sample.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    save_as_file(sorting(data), 'data/Database of Sample.json')
