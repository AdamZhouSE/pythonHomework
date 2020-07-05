"""
检测代码文件中不是python的部分
"""

import os


def detect_cpp(filename):  # 检测C++代码: 代码中有头文件或者注释方法使用了//
    with open(filename) as fp:
        content_list = fp.readlines()
        for content in content_list:
            content = content.strip()
            if content.startswith("#include"):
                print(content)
                return True
            if content.startswith("//"):
                print(content)
                return True
    return False


def count_file():  # 读取文件
    cnt = 0
    cases = os.listdir(os.getcwd() + "/CodeRecords")
    for dir_case in cases:
        if dir_case != ".DS_Store":
            # print(dir_case)
            users = os.listdir(os.getcwd() + "/CodeRecords/" + dir_case)
            for dir_user in users:
                if dir_user != ".DS_Store":
                    for file in os.listdir(os.getcwd() + "/CodeRecords" + "/" + dir_case + "/" + dir_user):
                        filename = os.getcwd() + "/CodeRecords" + "/" + dir_case + "/" + dir_user + "/" + file
                        if detect_cpp(filename):
                            # print(fileName)
                            cnt += 1
    print(cnt)


if __name__ == '__main__':
    count_file()
