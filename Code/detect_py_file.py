"""
检测提交中不是python的代码
1. 代码使用头文件#include
2. 代码使用非python注释 // 或 /* 或 <!---->
3. 非python类声明 public private protected
"""

import os


def detect_no_py(filename):  # 检测非python代码
    with open(filename, encoding="utf-8") as fp:
        content_list = fp.readlines()
        for content in content_list:
            content = content.strip()
            # 单独使用头文件判断 1429
            if content.startswith("#include"):
                # print(content)
                return True
            # 1491
            if content.startswith("//") or content.startswith("/*") or content.startswith("<!--"):
                # print(content)
                return True
            if content.startswith("private") or content.startswith("public") or content.startswith("protected"):
                # print(content)
                return True
            # 1543
            if content.startswith("exec(bytes.from"):
                # print(content)
                return True
            if content.startswith("if") and "//" in content and "(" in content and ":" not in content:
                print(content)
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
                        if detect_no_py(filename):
                            # print(fileName)
                            cnt += 1
    print("使用非python数量: ", cnt)
    print("题目总数: ", cnt_test)


if __name__ == '__main__':
    count_file()
