"""
代码行数统计
"""

import os

# 定义代码所在的目录
base_path = 'Code'


def collect_files(directory):  # 在指定目录下统计所有的py文件，以列表形式返回
    file_list = []
    for parent, dir_names, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                # 将文件名和目录名拼成绝对路径，添加到列表里
                file_list.append(os.path.join(parent, filename))
    return file_list


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


if __name__ == '__main__':
    filename = "Test/249310.py"
    total_code_num, total_blank_num, total_annotate_num = calc_line_num(filename)
    print(u'代码总行数为：  %s' % total_code_num)
    print(u'空行总行数为：  %s' % total_blank_num)
    print(u'注释行总行数为： %s' % total_annotate_num)
