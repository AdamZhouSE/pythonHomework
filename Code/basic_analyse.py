import json
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def save_as_file(data: dict, filename):
    with open(filename, 'w', encoding='utf-8')as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# 剔除异常数据
def delete(data: dict):
    for case_id, details in data.items():
        records = details["records"]

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
                    records[i]["is_cpp"] = final_record["is_cpp"]
                    records[i]["is_case-oriented"] = final_record["is_case-oriented"]
                    records[i]["num_of_line"] = final_record["num_of_line"]
                    del records[i]["upload_records"]
                except Exception as e:
                    print(case_id, "  ", records[i])
                    print(e)
            i += 1
    return data


def basic_analyse(data: dict):
    data = delete(data)
    for case_id, details in data.items():
        records = details["records"]
        grades = pd.Series([record["final_score"] for record in records])
        del data[case_id]["average_score"]
        data[case_id]["average"] = grades.mean()  # 平均值
        data[case_id]["median"] = grades.median()  # 中位数
        data[case_id]["var"] = grades.var()  # 方差
        data[case_id]["std"] = grades.std()  # 标准差
        data[case_id]["user_count"] = grades.count()  # 做题人数
    return data


if __name__ == '__main__':
    '''
    # 处理mooctest数据
    f = open('..//Data/Database of Mooctest.json', encoding='utf-8')
    data = json.loads(f.read())
    save_as_file(basic_analyse(data), '..//Data/updatedDatabase of Mooctest.json')
    f.close()
    '''

    # 调取题号为2061的数据
    f = open('..//Data/updatedDatabase of Mooctest.json', encoding='utf-8')
    data = json.loads(f.read())
    save_as_file(data["2061"], "2061.json")
