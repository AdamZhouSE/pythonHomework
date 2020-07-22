"""
数据测试
问题：当代码为0时无法检测面向用例和cpp
共计84203分提交
问题数据:
数据损坏:2份
压缩包错误,无法解压
case_id user_id upload_id
2528 60765 284171
2398 49823 308630

388份代码行数为0,无法检测
830份cpp
682份抄袭
"""


import json


if __name__ == "__main__":
    filename = "../Data/Database of Mooctest.json"
    with open(filename, 'r', encoding='utf-8') as f:
        res = f.read()
        data = json.loads(res)
        cnt_cpp = 0
        cnt_case_ori = 0
        cnt_blank = 0
        cnt_all = 0
        cnt_num = 0
        cnt_url = 0
        cnt_code_num = 0
        for case_id, details in data.items():
            records = details["records"]
            for record in records:
                user_id = record["user_id"]
                for up in record["upload_records"]:
                    if "is_cpp" not in up and "is_case-oriented" not in up and "num_of_line" in up:
                        cnt_blank += 1
                        cnt_code_num += up["num_of_line"]
                    if "is_cpp" in up:
                        cnt_cpp += 1
                    if "is_case-oriented" in up:
                        cnt_case_ori += 1
                    if "num_of_line" not in up:
                        print(case_id, user_id, up["upload_id"])
                        cnt_num += 1
                    cnt_all += 1

        print(cnt_blank)
        print(cnt_code_num)