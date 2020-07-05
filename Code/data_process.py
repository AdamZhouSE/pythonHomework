"""
数据处理
1. 转化数据格式,将json文件从以user为id变为以case为id
2. 将代码行数统计，面向用例，是否为cpp代码的结果写入json文件
"""

import json
import numpy as np
import pandas as pd
import cal_num_of_line as cl
import detect_if_else_structure as ds
import detect_py_file as df

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


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def analyse(data: list):
    for case_id, details in data.items():
        records = details["records"]
        data[case_id]["total_upload_times"] = sum([record["upload_times"] for record in records])
        data[case_id]["average_score"] = sum([record["final_score"] for record in records]) / len(records)
        data[case_id]["user_count"] = len(records)

        # 检测代码行数 & 面向用例情况
        for record in records:
            user_id = record["user_id"]
            for up in record["upload_records"]:
                upload_id = str(up["upload_id"])
                filepath = 'CodeRecords//' + case_id + "//" + user_id + "//" + upload_id + ".py"
                try:
                    # 代码行数
                    lst = cl.calc_line_num(filepath)
                    up["num_of_line"] = lst[0]

                    # 面向用例情况
                    flag, percentage = ds.cal_if_else_structure(filepath)
                    up["is_case-oriented"] = flag

                    # 检测是否为cpp代码
                    flag_cpp = df.detect_cpp(filepath)
                    up["is_cpp"] = flag_cpp
                except:
                    continue
    return data


if __name__ == '__main__':
    f = open('../Data/test_data.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    save_as_file(sorting(data), '../Data/Database of Mooctest.json')

    # f = open('data/sample.json', encoding='utf-8')
    # res = f.read()
    # data = json.loads(res)
    # save_as_file(sorting(data), 'data/Database of Sample.json')
