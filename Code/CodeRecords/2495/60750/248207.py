
import ast

def solve():
    data = input()
    dict_list = ast.literal_eval(input())
    res = []
    length = []
    for i in range(0,len(dict_list)):
        j = 0
        tmp = data * 1
        tmp_changed = False
        while j < len(dict_list[i]):
            if dict_list[i][j] not in tmp:
                break
            else:
                if j == len(dict_list[i]) - 1:
                    res.append(dict_list[i])
                    length.append(len(dict_list[i]))
                    break
                if tmp.index(dict_list[i][j]) + 1 == len(tmp):
                    break
                tmp = tmp[tmp.index(dict_list[i][j]) + 1:]
                j += 1


    tmp_len = sorted(length,reverse=True)
    print(res[length.index(tmp_len[0])])

solve()

