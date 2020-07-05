import sys

sys.setrecursionlimit(1000000)
nums = int(input())
str_letter = input()
base_list = []
for i in range(nums):
    base = input()
    base_list.append(base)


def cover(str_ope, str_list, cnt, offset):
    temp_list = []
    for i in range(offset + 1):
        temp = str_ope[i:]
        temp_list.append(temp)
    for ch in str_list:
        if ch in temp_list:
            cnt = cnt + 1
            return cnt
    dict_match = {}
    for i in range(offset + 1):
        for j in range(len(str_list)):
            temp = temp_list[i]
            if temp.startswith(str_list[j]) and len(str_list[j]) - (offset - i) > 0:
                dict_match[str_list[j][offset:]] = len(str_list[j][offset:])
    list_match = sorted(dict_match.items(), key = lambda x:x[1], reverse = True)
    maxMatch = list_match[0][0]
    offset = list_match[0][1] - 1
    cnt = cnt + 1
    cnt = cover(str_ope[offset + 1:], str_list, cnt, offset)
    return cnt


print(cover(str_letter, base_list, 0, 0))