"""
题目描述
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

输入描述
一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s 中只含有小写英文字母
输出描述
返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
"""


def process_set(str_lst, index):
    lst = []
    for i in index:
        lst.append(str_lst[i])
    lst = sorted(lst)
    count = 0
    for i in index:
        str_lst[i] = lst[count]
        count = count + 1
    return str_lst


string = input()
str = list(string)

pairs = eval(input())
list = []
for i in range(0, len(pairs)):
    a = pairs[i][0]
    b = pairs[i][1]
    exist = False
    for j in range(0, len(list)):
        if (a in list[j]) or (b in list[j]):
            list[j].add(a)
            list[j].add(b)
            exist = True
            break
    if not exist:
        new_set = set()
        new_set.add(a)
        new_set.add(b)
        list.append(new_set)
for i in range(0, len(list)):
    str = process_set(str, list[i])
ans = "".join(str)
print(ans)