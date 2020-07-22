"""
汇总了所有的统计前检测方法
包括检测是否抄袭，是否是非python代码，是否是面向用例
以便处理数据时调用
"""

import difflib
import os


# 检测抄袭答案
def detect_is_answer(answerpath, codepath):
    def extract_file(filepath):
        with open(filepath, encoding='utf-8') as f:
            # 预处理，将空行和注释行去除
            text = ''
            content_list = f.readlines()
            for content in content_list:
                content = content.lstrip()
                if content:
                    if not content.startswith("#"):
                        text += content
            # print(text)
            return text

    def get_similarity_ratio(s, t):
        return difflib.SequenceMatcher(None, s, t).quick_ratio()

    similarity_ratio = get_similarity_ratio(extract_file(answerpath), extract_file(codepath))
    # print(similarity_ratio)
    if similarity_ratio >= 0.9:
        return True
    else:
        return False


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


# 统计有效代码行数
def calc_line_num(file):  # 计算单个文件内的代码行数
    with open(file, encoding='utf-8') as fp:
        content_list = fp.readlines()
        file_code_num = 0  # 当前文件代码行数计数变量
        file_blank_num = 0  # 当前文件空行数计数变量
        file_annotate_num = 0  # 当前文件注释行数计数变量
        for content in content_list:
            content = content.strip()
            # 统计空行
            if content == '':
                file_blank_num += 1
            # 统计注释行
            elif content.startswith('#'):
                file_annotate_num += 1
            # 统计代码行
            else:
                file_code_num += 1
    # 返回代码行数，空行数，注释行数
    return file_code_num, file_blank_num, file_annotate_num


# 检测面向用例
def detect_is_case_orinted(file):
    with open(file, encoding='utf-8') as fp:
        content_list = fp.readlines()
        num_of_print = 0  # 打印行数
        num_of_code = 0  # 代码行数
        for content in content_list:
            content = content.lstrip()
            if content:
                if not content.startswith("#"):
                    num_of_code += 1
                    if content.startswith("print"):
                        num_of_print += 1
        if num_of_code == 0:  # 文件为空
            return False
        else:
            proportion_of_print = num_of_print/num_of_code
            # print(proportion_of_print)
            if proportion_of_print > 0.3:  # 当print语句占比大于0.3时，判定为面向用例
                return True
            else:
                return False


if __name__ == "__main__":
    os.chdir(os.getcwd()+"//Test")
    for filename in os.listdir():
        print(filename)
        print(detect_is_case_orinted(os.getcwd()+"//"+filename))
