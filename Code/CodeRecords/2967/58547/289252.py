def gcss(now_str, string):
    # return greatest common substring
    # 建立二维数组，找最大值
    # ref: https://blog.csdn.net/u010397369/article/details/38979077
    table = [[0 for y in range(0, len(now_str))] for x in range(0, len(string))]
    # row direction is now_str
    # col direction is string

    max_index = [-1, -1]
    max_len = 0
    i = 0
    while i < len(string):
        j = 0
        while j < len(now_str):
            if string[i] == now_str[j]:
                if i == 0 or j == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = table[i - 1][j - 1] + 1

                if table[i][j] > max_len:
                    max_len = table[i][j]
                    max_index = [i, j]
            j += 1
        i += 1

    return now_str[max_index[1] - max_len + 1: max_index[1] + 1]


def func():
    line_num = int(input())
    str_lib = []
    i = 0
    while i < line_num:
        str_lib.append(input())
        i += 1

    now = str_lib[0]
    i = 1
    while i < line_num:
        now = gcss(now, str_lib[i])
        i += 1

    print(len(now))


func()
