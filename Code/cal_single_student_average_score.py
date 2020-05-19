import json
import numpy as np
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def calAverage(data: dict):
    users = list(data.keys())
    sortings = {'线性表': 32, '排序算法': 11, '数字操作': 35, '字符串': 17, '数组': 44, '查找算法': 21, '树结构': 28, '图结构': 12}
    info = {'用户': users}
    print(info)
    df = pd.DataFrame(info, index=range(1, len(users) + 1),
                      columns=['用户', '完成度', '平均分', '已做平均分',
                               '查找算法', '树结构', '排序算法', '数字操作', '线性表', '图结构', '数组', '字符串'])
    for user_id, cases in data.items():
        cases = cases['cases']
        sum_score = sum(case['final_score'] for case in cases)
        df.loc[df['用户'] == user_id, '完成度'] = len(cases)
        df.loc[df['用户'] == user_id, '平均分'] = round(sum_score / 200, 2)
        df.loc[df['用户'] == user_id, '已做平均分'] = round(sum_score / len(cases), 2)

        # 分类统计
        for setName, numOfProblems in sortings.items():
            sum_score = sum(case['final_score'] for case in cases if case['case_type'] == setName)
            df.loc[df['用户'] == user_id,setName] = round(sum_score / sortings[setName], 2)

    df = df.sort_values(by='完成度', ascending=False)
    print(df)
    df.to_excel('test_data.xlsx', index=False, encoding='utf-8')


if __name__ == '__main__':
    f = open('test_data.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    calAverage(data)
