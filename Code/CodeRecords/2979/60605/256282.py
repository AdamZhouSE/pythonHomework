# 题目描述
# 字符串可是比赛经常出的问题，那么给大家出一个题，
#
# 输入五个字符串，输出5个字符串当中最长的字符串。每个字符串长度在100以内，且全为小写字母，如果一样，取第一个。
li = input().strip().split()
maxLen = 0
for i in li:
    maxLen = max(maxLen, len(i))
for i in li:
    if len(i) == maxLen:
        print(i)
        break