"""
题目描述

Oliver为了学好英语决定苦背单词，但很快他发现要直接记住杂乱无章的单词非常困难，他决定对单词进行分类。

两个单词可以分为一类当且仅当组成这两个单词的各个字母的数量均相等。

例如“AABAC”，它和“CBAAA”就可以归为一类，而和“AAABB”就不是一类。

现在Oliver有N个单词，所有单词均由大写字母组成，每个单词的长度不超过100。你要告诉Oliver这些单词会被分成几类。

输入描述

输入文件的第一行为单词个数N，以下N行每行为一个单词。
输出描述

输出文件仅包含一个数，表示这N个单词分成的类数

"""
n = eval(input())
a = []
for i in range(n):
    s = input()
    a.append(s)

for i in range(len(a)):
    a[i] = sorted(a[i])

ans = 1
a = sorted(a)
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        ans += 1

print(ans, end="")
