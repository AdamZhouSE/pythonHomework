"""
检测提交中不是python的代码
"""

import os


def detect_cpp(filename):  # 检测C++代码: 代码中有头文件或者注释方法使用了//
    with open(filename, encoding="utf-8") as fp:
        content_list = fp.readlines()
        for content in content_list:
            content = content.strip()
            # 单独使用头文件判断 1429
            if content.startswith("#include"):
                # print(content)
                return True
            if content.startswith("//"):
                # print(content)
                return True
    return False


def count_file():  # 读取文件夹,便于测试
    cnt = 0
    cnt_test = 0
    cases = os.listdir(os.getcwd() + "/CodeRecords")
    for dir_case in cases:
        if dir_case != ".DS_Store":
            # print(dir_case)
            cnt_test += 1
            users = os.listdir(os.getcwd() + "/CodeRecords/" + dir_case)
            for dir_user in users:
                if dir_user != ".DS_Store":
                    for file in os.listdir(os.getcwd() + "/CodeRecords" + "/" + dir_case + "/" + dir_user):
                        filename = os.getcwd() + "/CodeRecords" + "/" + dir_case + "/" + dir_user + "/" + file
                        if detect_cpp(filename):
                            # print(fileName)
                            cnt += 1
    print("使用C++数量: ", cnt)
    print("题目总数: ", cnt_test)


if __name__ == '__main__':
    count_file()
