"""
遗传算法组卷基本步骤
（详细内容见研究报告）
编码:实数编码
适应度函数
选择:轮盘赌算法
交叉:自适应交叉 多点交叉
变异:自适应变异
结束
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


def init_population(data, num):
    """
    初始化种群
    :param data: json数据
    :param num: 试卷期望试题数量
    :return: 初始的种群
    """
    population = []
    for i in range(0, 50): # 初始化种群，生成50个个体
        population.append(get_individual(data, num))
    return population


def selection(data, father, expect):
    """
    选择算子 采用轮盘赌算法
    :param data: json数据
    :param father: 父代种群
    :param expect: 期望难度
    :return:
    """
    population = father
    fitness = []
    cases = get_cases_degrees(data)
    for po in population: # 计算每个个体的适应度
        bias = 0
        for ty in po: # 个体的不同类别
            for cid in ty:
                bias += abs(cases.get(cid))/expect # 目标函数
        fitness.append(1.0/bias)
    print("适应度", fitness)
    selection_probability = []
    for fi in fitness:
        selection_probability.append(fi/np.sum(fitness))
    print("选择概率", selection_probability)
    cumulative_probability = []
    for i in range(0, len(fitness)):
        cumulative_probability.append(np.sum(selection_probability[0:i+1]))
    cumulative_probability[len(fitness)-1] = 1.0
    print("累积概率", cumulative_probability)
    selection_res = []
    fitness_res = []
    for i in range(0, 50):
        r = random.uniform(0, 1)
        for j in range(0, len(cumulative_probability)):
            if population[j] not in selection_res and cumulative_probability[j] >= r:
                selection_res.append(population[j])
                fitness_res.append(fitness[j])
    print("选择结果", selection_res)
    print(len(selection_res))
    return selection_res, fitness_res


def crossover(selection_res, fitness_res):
    """
    交叉 适用自适应交叉概率
    不同类型 多点交叉
    如果出现重复，则取消交叉操作
    :param selection_res: 选择结果
    :param fitness_res: 当前种群每个个体的适应度
    :return: 交叉结果，适应度
    """
    f_avg = np.mean(fitness_res)
    f_max = np.max(fitness_res)
    for i in range(0, len(selection_res)//2):
        i1 = len(selection_res)-1-i # 第i个个体和第n-i个个体交叉
        fm = max(fitness_res[i], fitness_res[i1])
        pc = 0.9
        if fm >= f_avg: # 自适应交叉概率
            pc = abs(0.9 - (0.9-0.6) * (fm-f_avg) / (f_max-f_avg))
        r = random.uniform(0, 1)
        if r < pc:
            for j in range(0, 8):
                start = len(selection_res[i][j])//2
                temp = selection_res[i][j][start:]
                selection_res[i][j][start:] = selection_res[i1][j][start:]
                selection_res[i1][j][start:] = temp
                check = set(selection_res[i][j])
                if len(check) != len(selection_res[i][j]): # 出现重复题号，取消交叉操作
                    temp = selection_res[i][j][start:]
                    selection_res[i][j][start:] = selection_res[i1][j][start:]
                    selection_res[i1][j][start:] = temp
                # else:
                #     print(i, end=" ")
    crossover_res = selection_res
    # print()
    print("交叉结果", crossover_res)
    return crossover_res


def mutation(data, crossover_res, fitness_res):
    """
    变异 自适应变异概率
    不同类型分别进行变异，从题库中随机抽出一道题进行替换
    如果出现重复，则取消该次操作
    :param data: json数据
    :param crossover_res: 交叉结果
    :param fitness_res:
    :return:
    """
    cases = get_types(data) # 获取分类题目
    f_avg = np.mean(fitness_res)
    f_max = np.max(fitness_res)
    for i in range(0, len(crossover_res)):
        pm = 0.1
        if fitness_res[i] >= f_avg: # 获取自适应变异概率
            pm = abs(pm - (0.1-0.001)*(f_max-fitness_res[i])/(f_max-f_avg))
        r = random.uniform(0, 1)
        if r < pm:
            for j in range(0, len(crossover_res[i])):
                change_from = random.randint(0, len(crossover_res[i][j])-1) # 被替换的题的下标
                change_to = random.randint(0, len(cases[j])-1) # 从题库中随机抽取的题的下标
                if cases[j][change_to] not in crossover_res[i][j]:
                    crossover_res[i][j][change_from] = cases[j][change_to]
                    # print(i, end=" ")
    mutation_res = crossover_res
    # print()
    print(mutation_res)
    print("平均适应度", f_avg)
    return mutation_res


def get_individual(data, num): # 获取个体
    cases = get_types(data)
    # cnt = [] # 可自定义不同类型题目数量
    res = []
    for i in range(0, 8): # 获取一个个体
        res.append(get_encode(cases[i], int(len(cases[i]) / 882 * num)))  # 某一类别 生成多少题目
    return res


def get_encode(data, num): # 获取一定数量的某一个类别的编码
    res = []
    flag = 0
    while flag < num:
        index = random.randint(0, len(data)-1)
        if index not in res:
            flag += 1
            res.append(data[index])
    return res


def get_matrix(data):
    cases = []  # 目标矩阵
    for type_name, details in data.items():
        print(type_name, len(details["cases"]))
        for case_id, case in details["cases"].items():
            cases.append([case["case_id"], case["case_type"], case["degree"], case["difficulty"]])
    return cases


def get_types(data): # 将不同类别的题目id分开存放
    cases = []
    for type_name, details in data.items():
        m_type = []
        for case_id, case in details["cases"].items():
            m_type.append(case["case_id"])
        cases.append(m_type)
    return cases


def get_cases_degrees(data): # 获取以题号为单位的字典
    cases = {}
    for type_name, details in data.items():
        for case_id, case in details["cases"].items():
            cases[case_id] = case["degree"]
    return cases


if __name__ == "__main__":
    with open("../Data/result.json", 'r', encoding="utf-8") as f:
        _data = json.loads(f.read())
        _population = init_population(_data, 200)
        # sRes, fitRes = selection(_data, _population, 2.6)
        # cRes, fitRes = crossover(sRes, fitRes)
        # mRes, fitRes = mutation(_data, cRes, fitRes)
        for t in range(0, 1000):
            sRes, fitRes = selection(_data, _population, 2.66)
            cRes = crossover(sRes, fitRes)
            mRes = mutation(_data, cRes, fitRes)
            _population = mRes
    papers = []
    for t in range(0, len(_population)):
        paper = []
        for tt in range(0, 8):
            for ttt in range(0, len(_population[t][tt])):
                paper.append(_population[t][tt][ttt])
        papers.append(paper)
    cases_de = get_cases_degrees(_data)
    for pa in papers:
        degrees = []
        for cid in pa:
            degrees.append(cases_de[cid])
        print(np.mean(degrees))
