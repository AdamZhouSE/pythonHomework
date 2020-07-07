import json
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def basic_analyse(data: dict):
    for case_id, details in data.items():
        records = details["records"]

        # 删去upload_records
        for record in records:
            del record["upload_records"]

        grades = pd.Series([record["final_score"] for record in records])
        data[case_id]["average"] = grades.mean()  # 平均值
        data[case_id]["median"] = grades.median()  # 中位数
        data[case_id]["var"] = grades.var()  # 方差
        data[case_id]["std"] = grades.std()  # 标准差
        data[case_id]["user_count"] = len(records)  # 做题人数
    return data


if __name__ == '__main__':

    # 处理mooctest数据
    with open('..//Data/Database of MOOctest.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        save_as_file(basic_analyse(data), '..//Data/updatedDatabase of MOoctest.json')
    '''
    # 调取题号为2061的数据
    f = open('../Data/updatedDatabase of Mooctest.json', encoding='utf-8')
    data = json.loads(f.read())
    save_as_file(data["2061"], "2061.json")
    f.close()
    '''

