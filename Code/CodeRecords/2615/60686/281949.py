nums = int(input())
list_all = []
for i in range(nums):
    str_input = input()
    list_all.append(str_input)
for i in range(nums):
    res = ""
    str_input = list_all[i]
    judge_list = [False] * 26
    for j in range(len(str_input)):
        judge_list[ord(str_input[j]) - ord('A')] = True
    for differ in range(1, 26):
        for first in range(25, -1, -1):
            if judge_list[first]:
                temp = "" + chr(ord('A') + first)
                for next_in in range(first - differ, -1, -differ):
                    if judge_list[next_in]:
                        temp += chr(ord('A') + next_in)
                    else:
                        break
                if len(temp) > len(res):
                    res = temp
    print(res)
