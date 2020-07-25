"""
基本分析
求出每道题的平均值，中位数，标准差，做题人数和实际通过人数
汇总为final_data.json
数据格式示例:
"2081": {
        "case_id": "2081",
        "case_type": "字符串",
        "total_upload_times": 81,
        "user_count": 45,
        "num_of_isanswer": 0,  是否抄袭
        "num_of_iscpp": 0, 是否是非python代码
        "num_of_isco": 2,  是否是面向用例
        "num_of_isiv": 2,  总计无效代码数量
        "difficulty": 2,   预估难度
        "planed_usercount": 47,
        "average": 100.0,
        "num_of_full-score": 45,
        "num_of_valid_full-score": 43,
        "pass_rate": 0.9148936170212766
        "avg_lines": 平均行数
    },
"""

import json
import pandas as pd
import numpy as np

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def basic_analyse(data: dict):
    avg_lines = get_lines()
    i = 0
    for case_id, details in data.items():
        records = details["records"]

        # 删去upload_records
        for record in records:
            del record["upload_records"]

        grades = pd.Series([record["final_score"] for record in records])
        details["average"] = grades.mean()  # 平均值
        details["median"] = grades.median()  # 中位数
        details["std"] = grades.std()  # 标准差
        details["user_count"] = len(records)  # 做题人数
        details["num_of_full-score"] = int(grades.value_counts()[100])  # 计算满分人数
        details["num_of_valid_full-score"] = details["num_of_full-score"] - details["num_of_isiv"]  # 计算实际满分人数
        details["pass_rate"] = details["num_of_valid_full-score"]/details["planed_usercount"]
        details["avg_lines"] = avg_lines[i]
        i += 1
    return data


def get_lines(): # 获取代码行数
    lines = []
    with open("../Data/updatedDatabase of Mooctest.json", 'r', encoding="utf-8") as fi:
        data = json.loads(fi.read())
        for case_id, details in data.items():
            for record in details["records"]:
                lines.append([case_id, record["num_of_line"]])
    print(lines)
    res = []
    for case_id, details in data.items():
        res.append(get_avg_lines(case_id, lines))
    print(res)
    return res


def get_avg_lines(cid, data):
    avg = []
    for i in range(0, len(data)):
        if cid == data[i][0]:
            avg.append(data[i][1])
    return np.mean(avg)


if __name__ == '__main__':
    # 处理mooctest数据
    with open('..//Data/Database of Mooctest.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        save_as_file(basic_analyse(data), '..//Data/updatedDatabase of Mooctest.json')

    # 调取题号为2061的数据
    with open('../Data/updatedDatabase of Mooctest.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        data = data["2061"]
        save_as_file(data, '2061.json')

    # 调取题号为2761的数据
    with open('../Data/updatedDatabase of Mooctest.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        data = data["2761"]
        save_as_file(data, '2761.json')

    with open('../Data/updatedDatabase of Mooctest.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        for case_id, details in data.items():
            for name in ["case_zip", "records",  "group", "median", "std"]:
                del details[name]
    save_as_file(data, "../Data/simplifyDatabase.json")
