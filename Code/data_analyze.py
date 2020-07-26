"""
数据分析
详细研究过程见研究报告
"""

import json
import pandas as pd
import numpy as np
from decimal import Decimal

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def get_difficulty(data):
    d = [] # 题目难度
    u = [] # 上传率
    li = [] # 代码行数
    avg = []
    avg_all = [] # 算术平均数
    num_of_cases = []
    for types in data.items():
        avg.append(types[1]["avg_pass_rate"])
        cor_pu = (types[1]["correlation_pu"]) # 通过率与上传率的相关系数
        cor_pl = (types[1]["correlation_pl"]) # 通过率与代码行数的相关系数
        for cases in types[1].items(): # 类别
            if cases[0] == 'cases':
                print(types[0], len(cases[1]))
                num_of_cases.append([types[0], len(cases[1])])
                for case in cases[1].items():
                    u.append(case[1]["up_rate"]*cor_pu)
                    li.append(case[1]["avg_lines"]*cor_pl)
                    d.append((1 - case[1]["pass_rate"]))  # 1-该题通过率
                    avg_all.append(case[1]["pass_rate"])
    # 映射到区间[1,5]
    d1 = map_to(1, 5, d) # 映射后的试题难度
    u1 = map_to(1, 5, u)
    li1 = map_to(1, 5, li)
    final_d = []
    for i in range(0, len(d1)):
        # 用上传次数和代码行数进行修正
        final_d.append(get_final_d(d1[i], u1[i], li1[i], 0.846, 0.084))
    cnt_easy = 0
    cnt_medium = 0
    cnt_hard = 0
    for di in final_d:
        if 1 <= di < 2.2: # 通过率70% easy
            cnt_easy += 1
        elif 2.2 <= di < 3.4: # 通过率70%-40% medium
            cnt_medium += 1
        else: # 通过率40%以下 hard
            cnt_hard += 1
    print("easy: ", cnt_easy, cnt_easy/882)
    print("medium: ", cnt_medium, cnt_medium/882)
    print("hard: ", cnt_hard, cnt_hard/882)
    print("难度系数均值:", np.mean(final_d))
    print("修正前通过率均值:", np.mean(avg_all))
    print("修正后均值:", 1-np.mean(map_to(0, 1, final_d)))
    print(avg)
    return final_d


def get_final_d(k, m, n, alpha, beta): # 获取修正后的难度系数
    return alpha*k + beta*m + (1-alpha-beta)*n


def get_diff_by_degree(degree): # 根据难度系数获取题目难度
    if 1 <= degree < 2.2:
        return "easy"
    elif 2.2 <= degree < 3.4:
        return "medium"
    else:
        return "hard"


def geometric_mean(data):  # 计算几何平均数
    total = 1
    for i in data:
        if i == 0:
            continue
        total *= Decimal(str(format(i, ".2f")))
        # print(float(format(i, ".2f")))
    return total ** Decimal(1.0/len(data))


def map_to(start, end, data): # 将数据映射到指定区间
    d_min = np.min(data)
    d_max= np.max(data)
    res = []
    for d in data:
        res.append(start+(end-start)/(d_max-d_min)*(d-d_min))
    return res


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
        # save_as_file(result, "../Data/result.json")
