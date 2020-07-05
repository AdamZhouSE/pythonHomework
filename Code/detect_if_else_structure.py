"""
检测面向用例情况
if-elif-else结构（包括内部的内容）占该题总行数的40%
"""
import os


def cal_if_else_structure(file):  # 统计if-else结构的数量
    with open(file) as fp:
        content_list = fp.readlines()
        # print(content_list)
        content_list_code = []  # 取出所有的有效代码行
        file_code_num = 0
        file_if_else_num = 0
        # 统计代码行数
        index = 0
        for content in content_list:
            content = content.strip()
            if content != '' and not content.startswith("#"):
                file_code_num += 1
                content_list_code.append(content_list[index])
            index += 1
        length = len(content_list_code)
        # 统计if-else结构
        for i in range(0, length):
            if "if" in content_list_code[i] or "elif" in content_list_code[i] or "else" in content_list_code[i]:
                file_if_else_num += 1
                count_blank = 0  # 统计句首的空格数
                # print(content_list_code[i])
                for j in range(0, len(content_list_code[i])):
                    if content_list_code[i][j] == " ":
                        count_blank += 1
                    else:
                        break
                print("if-else句首空格", count_blank)
                # 统计内部内容，句首空格数大于if-else结构的句首空格数
                for j in range(i+1, length):
                    count_in_blank = 0
                    for k in range(0, len(content_list_code[j])):
                        if content_list_code[j][k] == " ":
                            count_in_blank += 1
                        else:
                            break
                    print("内部空格", count_in_blank)
                    if count_in_blank > count_blank:
                        file_if_else_num += 1
                    else:
                        break
        print(file_code_num, file_if_else_num)
        per = file_if_else_num/file_code_num
        if per > 0.4:
            return True, per
        else:
            return False, per


if __name__ == "__main__":
    res, percent = cal_if_else_structure("Test/test_if_else.py")
    print(res, percent)


