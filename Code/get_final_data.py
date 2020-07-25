"""
以题目类别作为分类标准处理数据
最终数据格式
"type_name": {
        "case_id": {
            "case_id": "2081",
            "case_type": "字符串",
            "up_rate": 1.8,  上传总数/实际做题人数
            "pass_rate": 0.9148936170212766
            "avg_lines":
        },
"""

import json
import pandas as pd
import os
import numpy as np
from scipy import stats


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
                                                         "pass_rate": details["pass_rate"],
                                                         "avg_lines": details["avg_lines"]}
    return res


def get_data_plus(types):
    res = {}
    for type_name, cases in types.items():
        if type_name not in res.keys():
            res[type_name] = {"cases": cases}
        sum_of_up_rate = pd.Series([case["up_rate"] for case_id, case in cases.items()])
        res[type_name]["avg_up_rate"] = geometric_mean(sum_of_up_rate) # 平均比率-几何平均数
        res[type_name]["mid_up_rate"] = sum_of_up_rate.median() # 中位数
        res[type_name]["mode_up_rate"] = stats.mode(sum_of_up_rate)[0][0] # 求众数
        res[type_name]["std_up_rate"] = sum_of_up_rate.std() # 标准差
        sum_of_pass_rate = pd.Series([case["pass_rate"] for case_id, case in cases.items()])
        res[type_name]["avg_pass_rate"] = geometric_mean(sum_of_pass_rate)
        res[type_name]["mid_pass_rate"] = sum_of_pass_rate.median()
        res[type_name]["mode_pass_rate"] = stats.mode(sum_of_pass_rate)[0][0]
        res[type_name]["std_pass_rate"] = sum_of_pass_rate.std()
        res[type_name]["correlation_pu"] = sum_of_up_rate.corr(sum_of_pass_rate) # 通过率与上传率的相关系数
        sum_of_lines = pd.Series([case["avg_lines"] for case_id, case in cases.items()])
        res[type_name]["avg_lines"] = sum_of_lines.mean() # 算术平均数
        res[type_name]["mid_lines"] = sum_of_lines.median()
        res[type_name]["mode_lines"] = stats.mode(sum_of_lines)[0][0]
        res[type_name]["std_lines"] = sum_of_lines.std()
        res[type_name]["correlation_pl"] = sum_of_lines.corr(sum_of_pass_rate) # 通过率与代码行数的相关系数
    return res


def geometric_mean(data):  # 计算几何平均数
    total = 1
    for i in data:
        # 遇到通过率是0时，赋予一个极小值
        if i == 0:
            i = 0.0000000001
        total*=i
    return pow(total,1/len(data))


if __name__ == "__main__":
    # typeName = ['字符串', '线性表', '查找算法', '数组', '数字操作', '树结构', '排序算法', '图结构']
    with open("../Data/simplifyDatabase.json", 'r', encoding="utf-8") as f:
        _data = json.loads(f.read())
        _data = get_data(_data)
        save_as_file(_data, "../Data/final_data.json")
    with open("../Data/final_data.json", 'r', encoding="utf-8") as f:
        _data = json.loads(f.read())
        _data = get_data_plus(_data)
        save_as_file(_data, "../Data/final_data_v2.json")