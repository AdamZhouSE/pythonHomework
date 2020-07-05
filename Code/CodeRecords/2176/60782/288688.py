"""
题目要求
读入一个长度为n的由大小写英文字母或数字组成的字符串，请把这个字符串的所有非空后缀按字典序从小到大排序，然后按顺序输出后缀的第一个字符在原串
中的位置。位置编号为1到n。
"""
"""
输入描述
    一行一个长度为n的仅包含大小写英文字母或数字的字符串。
    数据范围：1≤n≤10^6
"""
"""
输出描述
    第一行n个整数，第i个整数为SA[i]。
"""


something = input()
dic = {}
word = []
for c in range(len(something)):
    dic.update({something[c:]:(c + 1)})
    word.append(something[c:])
word.sort()
for i in range(len(word) - 1):
    print(dic[word[i]],end=" ")