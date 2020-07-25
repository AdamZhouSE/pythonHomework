"""
数据分析
详细研究过程见研究报告
"""

import json
import pandas as pd
import os
import numpy as np

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def get_difficulty(data):
    d = [] # 题目难度
    u = [] # 上传率
    avg = []
    for types in data.items():
        avg.append(types[1]["avg_pass_rate"]) # 平均通过率
        cor = (types[1]["correlation"]) # 相关系数
        for cases in types[1].items(): # 类别
            if cases[0] == 'cases':
                for case in cases[1].items():
                    u.append(case[1]["up_rate"]*cor)
                    d.append((1 - case[1]["pass_rate"]))  # 1-该题通过率
    # 映射到区间[1,5]
    d_max = np.max(d)
    d_min = np.min(d)
    d1 = [] # 映射后的试题难度
    for di in d:
        d1.append(1+(5-1)/(d_max-d_min)*(di-d_min))
    u_max = np.max(u)
    u_min = np.min(u)
    u1 = []
    for ui in u:
        u1.append(1+(5-1)/(u_max-u_min)*(ui-u_min))
    final_d = []
    for i in range(0, len(d1)):
        # 在整体通过率稳定的情况下，用上传次数进行修正，将大家提交次数较多的题目难度提升
        final_d.append(get_final_d(d1[i], u1[i], 0.91))
    cnt_easy = 0
    cnt_medium = 0
    cnt_hard = 0
    for di in final_d:
        if 1 <= di < 2.2: # 通过率70% easy
            cnt_easy += 1
        elif 2.2 <= di < 3.4: # 通过率70%-40% medium
            cnt_medium += 1
        else: # 通过率40%一下 hard
            cnt_hard += 1
    print("easy: ", cnt_easy, cnt_easy/882)
    print("medium: ", cnt_medium, cnt_medium/882)
    print("hard: ", cnt_hard, cnt_hard/882)
    print("难度系数均值", np.mean(final_d))
    print("修正后均值", 1-(np.mean(final_d)-1)/4)
    print(np.mean(avg))
    return final_d


def get_final_d(m, n, alpha):
    return alpha*m + (1-alpha)*n


def get_diff_by_degree(degree):
    if 1 <= degree < 2.2:
        return "easy"
    elif 2.2 <= degree < 3.4:
        return "medium"
    else:
        return "hard"


def get_result(data, final_d):
    res = {}
    i = 0
    for types in data.items():
        if types[0] not in res.keys():
            res[types[0]] = {"cases": types[1]}
        for cid, case in types[1].items():
            res[types[0]]["cases"][cid] = case
            res[types[0]]["cases"][cid]["degree"] = final_d[i]
            res[types[0]]["cases"][cid]["difficulty"] = get_diff_by_degree(final_d[i])
            i += 1
    print(i)
    return res


if __name__ == "__main__":
    with open("../Data/final_data_v2.json", 'r', encoding="utf-8") as f:
        _data = json.loads(f.read())
        final_data = get_difficulty(_data)
    with open("../Data/final_data.json", 'r', encoding="utf-8") as f:
        _data = json.loads(f.read())
        result = get_result(_data, final_data)
        save_as_file(result, "../Data/result.json")