"""
数据处理
1. 转化数据格式,将json文件从以user为id变为以case为id
2. 将代码行数统计，面向用例，是否为cpp代码的结果写入json文件
"""

import json
import numpy as np
import pandas as pd
from Code import cal_num_of_line as cl
from Code import detect_if_else_structure as ds
from Code import detect_py_file as df
import os

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

        # 剔除upload_records为空的数据（异常）
        i = 0
        while i < len(records):
            if records[i]["upload_times"] == 0:
                print(case_id, "  ", records[i])
                del records[i]
                i -= 1
            else:
                try:
                    final_record = records[i]["upload_records"][-1]
                    records[i]["final_upload_id"] = final_record["upload_id"]
                    records[i]["final_code_url"] = final_record["code_url"]
                except Exception as e:
                    print(case_id, "  ", records[i])
                    print(e)
            i += 1

        data[case_id]["total_upload_times"] = sum([record["upload_times"] for record in records])
        data[case_id]["average"] = sum([record["final_score"] for record in records]) / len(records)
        data[case_id]["user_count"] = len(records)

        # 计算测试用例个数
        testcase_filepath = os.getcwd() + "\\Cases\\" + str(case_id) + '\\.mooctest\\testCases.json'
        try:
            with open(testcase_filepath, encoding='utf-8') as jsonf:
                testCases = json.loads(jsonf.read())
                data[case_id]["num_of_testCases"] = len(testCases)
        except:
            print(testcase_filepath, "损坏")

        # 检测代码行数 & 面向用例情况 & 是否为python
        num_of_iscpp = 0 # 非python计数
        num_of_isco = 0 # 面向用例计数
        for record in records:
            user_id = record["user_id"]
            upload_id = str(record["final_upload_id"])
            codepath = 'CodeRecords//' + case_id + "//" + user_id + "//" + upload_id + ".py"

            try:
                record["num_of_line"] = 0
                record["is_cpp"] = True
                record["is_case-oriented"] = True

                # 代码行数
                lst = cl.calc_line_num(codepath)
                record["num_of_line"] = lst[0]

                if record["num_of_line"] > 0:
                    # 检测是否为cpp代码
                    flag_cpp = df.detect_cpp(codepath)
                    record["is_cpp"] = flag_cpp
                    if flag_cpp:
                        num_of_iscpp+=1

                    # 面向用例情况
                    flag, percentage = ds.cal_if_else_structure(codepath)
                    record["is_case-oriented"] = flag
                    if flag_cpp == False and flag == True:
                        num_of_isco+=1
            except:
                continue

        # 记录面向用例、非python情况
        data[case_id]["num_of_iscpp"] = num_of_iscpp
        data[case_id]["num_of_isco"] = num_of_isco

    return data


if __name__ == '__main__':
    '''
    f = open('../Data/sample.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    save_as_file(sorting(data), '../Data/Database of Sample.json')
    '''

    f = open('../Data/test_data.json', encoding='utf-8')
    res = f.read()
    rootdata = json.loads(res)
    save_as_file(sorting(rootdata), '../Data/Database of Mooctest.json')
    f.close()
