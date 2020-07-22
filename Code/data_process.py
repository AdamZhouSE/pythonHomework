"""
数据处理
1. 转化数据格式,将json文件从以user为id变为以case为id
2. 将代码行数统计，面向用例，是否为cpp代码的结果写入json文件
"""

import json
import pandas as pd
from Code import dectect_all as da
import os

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def sorting(data: list):
    """
    将以用户为单位转换为以题目为单位
    :param data: 原始数据
    :return: 转换后的数据
    """
    data = delete_invaliduser(data)
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


def delete_invaliduser(data, casecount=10):
    """
    删除无效用户的记录（将做题数不足10题的用户判定为无效用户）
    :param data: 原始数据
    :param casecount: 做题数
    :return: 删除后的数据
    """
    newdata = {}
    for user_id, details in data.items():
        if user_id == "61097":
            i = 0
            while i < len(details["cases"]):
                if details["cases"][i]["case_id"] in {"2663", "2666", "2672"}:
                    del details["cases"][i]
                    i -= 1
                i += 1
        elif user_id == "60598":
            i = 0
            while i < len(details["cases"]):
                if details["cases"][i]["case_id"] in {"2061", "2127", "2179", "2307", "2438", "2701"}:
                    del details["cases"][i]
                    i -= 1
                i += 1
        if user_id != "47329" and len(details["cases"]) > casecount:
            newdata[user_id] = details
    save_as_file(newdata, "../Data/newtest_data.json")
    return newdata


def analyse(data: list):
    """
    在原始数据集上增加检测信息、基本统计信息
    :param data: 原始数据
    :return: 更新后的数据
    """
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
        num_of_iscpp = 0  # 非python计数
        num_of_isco = 0  # 面向用例计数
        num_of_isanswer = 0  # 与答案一致计数
        num_of_isiv = 0  # 无效代码计数
        for record in records:
            user_id = record["user_id"]
            upload_id = str(record["final_upload_id"])
            answerpath = 'Cases//' + case_id + "//.mooctest//answer.py"
            codepath = 'CodeRecords//' + case_id + "//" + user_id + "//" + upload_id + ".py"

            try:
                record["num_of_line"] = 0
                record["is_cpp"] = True
                record["is_case-oriented"] = True
                record["is_answer"] = True

                # 代码行数
                lst = da.calc_line_num(codepath)
                record["num_of_line"] = lst[0]

                if record["num_of_line"] > 0:
                    # 检测是否为答案
                    flag_answer = da.detect_is_answer(answerpath, codepath)
                    record["is_answer"] = flag_answer
                    if flag_answer:
                        num_of_isanswer += 1

                    # 检测是否为cpp代码
                    flag_cpp = da.detect_no_py(codepath)
                    record["is_cpp"] = flag_cpp
                    if flag_cpp:
                        num_of_iscpp += 1

                    # 面向用例情况
                    flag_co = da.detect_is_case_orinted(codepath)
                    record["is_case-oriented"] = flag_co
                    if flag_cpp == False and flag_co == True:
                        num_of_isco += 1

                # 判定是否无效
                if record["num_of_line"] == 0 \
                    or record["is_cpp"]\
                    or record["is_case-oriented"]\
                    or record["is_answer"]:
                    record["is_invalid"] = True
                    num_of_isiv +=1
            except Exception as e:
                print(e)
                continue

        # 记录面向用例、非python情况
        data[case_id]["num_of_isanswer"] = num_of_isanswer
        data[case_id]["num_of_iscpp"] = num_of_iscpp
        data[case_id]["num_of_isco"] = num_of_isco
        data[case_id]["num_of_isiv"] = num_of_isiv

    return merge_grouping(data)


def save_as_file(data: dict, filename):
    """
    存档
    :param data: 需要保存的数据（字典格式）
    :param filename: 应保存的文件名
    :return:
    """
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def merge_grouping(data: dict):
    with open('../Data/new_cases_information.json', encoding='utf-8') as f:
        cases = json.loads(f.read())
    for case_id, details in data.items():
        data[case_id]["group"] = cases[case_id]["group"]
        data[case_id]["difficulty"] = cases[case_id]["difficulty"]
        data[case_id]["planed_usercount"] = cases[case_id]["planed_usercount"]
    return data


if __name__ == '__main__':
    with open('../Data/test_data.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        save_as_file(sorting(data), '../Data/Database of Mooctest.json')
