"""
抽取n道题目，期望试卷难度系数为d
随机算法实现组卷
遗传算法实现组卷
"""
from enum import Enum
import json
import numpy as np
import random


class Type(Enum): # 枚举类 列举8个不同的类别
    STRING = "字符串"
    LINEAR = "线性表"
    ARRAY = "数组"
    SEARCH = "查找算法"
    SORT = "排序算法"
    MATH = "数字操作"
    GRAPH = "图结构"
    TREE = "树结构"


def get_matrix(data):
    cases = []  # 目标矩阵
    for type_name, details in data.items():
        for case_id, case in details["cases"].items():
            cases.append([case["case_id"], case["case_type"], case["degree"], case["difficulty"]])
    return cases


def random_generate(data, n, de): # 随机算法
    cases = get_matrix(data)
    paper = [] # 存储题目
    nums = [] # 存储题目在数组的下标，避免重复抽取
    judge = 0 # 判断是否抽到要求的题目数量
    flag = False # 组卷是否成功
    while judge < n:
        index = random.randint(0, len(cases)-1)
        if index not in nums:
            nums.append(index)
            paper.append(cases[index])
            judge += 1
    if check_paper(paper, de):
        flag = True
    return flag, paper


def check_paper(data, de): # 检查试卷是否符合约束条件
    degrees = []
    types = []
    for d in data:
        types.append(d[1])
        degrees.append(d[2])
    return check_case_degree(degrees, de) and check_case_types(types)


def check_case_degree(data, de): # 检查试卷难度
    diff = np.mean(data)
    # print(diff)
    if de-0.2 < diff < de+0.2:
        return True
    return False


def check_case_types(data): # 检查试卷题目类别
    res = {}
    flag = True
    for t in Type:
        per = data.count(t.value)/len(data)
        res[t.value] = per
        if per < 0.05 or per > 0.2:
            flag = False
            break
    # print(res)
    return flag


def detect_success_rate(data, cnt, de, times):
    results = []
    for i in range(0, times):
        res = random_generate(data, cnt, de)
        # if res[0]:
        #     return res[1]
        results.append(res[0])
    print(results.count(True))
    print(results.count(True)/times)


if __name__ == "__main__":
    with open("../Data/result.json", 'r', encoding="utf-8") as f:
        _data = json.loads(f.read())
    detect_success_rate(_data, 200, 2.66, 10000)


