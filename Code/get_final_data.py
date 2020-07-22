"""
以题目类别作为分类标准处理数据
最终数据格式
"type_name": {
        "case_id": {
            "case_id": "2081",
            "case_type": "字符串",
            "up_rate": 1.8,  上传总数/实际做题人数
            "pass_rate": 0.9148936170212766
        },
"""

import json
import pandas as pd
import os

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def get_data(cases):
    res = {}
    for case_id, details in cases.items():
        if details["case_type"] not in res.keys():
            res[details["case_type"]] = {details["case_id"]: {}}
        res[details["case_type"]][details["case_id"]] = {"case_id": details["case_id"],
                                                         "case_type": details["case_type"],
                                                         "up_rate": details["total_upload_times"]/details["user_count"],
                                                         "pass_rate": details["pass_rate"]}
    return res


def get_data_plus(types):
    res = {}
    for type_name, cases in types.items():
        if type_name not in res.keys():
            res[type_name] = {"cases": cases}
        sum_of_up_rate = pd.Series([case["up_rate"] for case_id, case in cases.items()])
        res[type_name]["avg_up_rate"] = sum_of_up_rate.mean()
        res[type_name]["mid_up_rate"] = sum_of_up_rate.median()
        res[type_name]["std_up_rate"] = sum_of_up_rate.std()
        sum_of_pass_rate = pd.Series([case["pass_rate"] for case_id, case in cases.items()])
        res[type_name]["avg_pass_rate"] = sum_of_pass_rate.mean()
        res[type_name]["mid_pass_rate"] = sum_of_pass_rate.median()
        res[type_name]["std_pass_rate"] = sum_of_pass_rate.std()
    return res


if __name__ == "__main__":
    # typeName = ['字符串', '线性表', '查找算法', '数组', '数字操作', '树结构', '排序算法', '图结构']
    with open("../Data/simplifyDatabase.json", 'r', encoding="utf-8") as f:
        data = json.loads(f.read())
        data = get_data(data)
        save_as_file(data, "../Data/final_data.json")
    with open("../Data/final_data.json", 'r', encoding="utf-8") as f:
        data = json.loads(f.read())
        data = get_data_plus(data)
        save_as_file(data, "../Data/final_data_v2.json")