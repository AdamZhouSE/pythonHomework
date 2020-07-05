"""
题目描述
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s == None or t == None:
        return False
    if s == "" and t == "":
        return True
    if len(s) != len(t):
        return False
    sett = set(t)
    for m in sett:
        if s.count(m) != t.count(m):
            return False
    return True


line1 = input().split("\"")
s = line1[1]
t = line1[3]
print(isAnagram(s, t))
