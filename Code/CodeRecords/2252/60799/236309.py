# 统计词频
import operator


def search(string):
    result_dict = {}
    for i in string:
        if i in result_dict.keys():
            result_dict[i] += 1
        else:
            result_dict[i] = 1
            # key=operator.itemgetter(0) ?
    return sorted(result_dict.items(), key=operator.itemgetter(0))


T = int(input())
for hhh in range(0, T):
    s = input()
    c = input()
    dict1 = search(c)
    num = 0
    for i in range(len(s) - len(c) + 1):  # +1
        if dict1 == search(s[i:i + len(c)]):
            num += 1
    print(num)