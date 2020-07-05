"""
题目描述
    佳媛姐姐过生日的时候，她的小伙伴从某东上买了一个生日礼物。生日礼物放在一个神奇的箱子中。箱子外边写了一个长为n的字符串s，和m个问题。
    佳媛姐姐必须正确回答这m个问题，才能打开箱子拿到礼物，升职加薪，出任 CEO，嫁给高富帅，走上人生巅峰。每个问题均有a,b,c,d四个参数，
    问你子串s[a...b]的所有子串和s[c...d]的最长公共前缀的长度的最大值是多少？佳媛姐姐并不擅长做这样的问题，所以她向你求助，你该如何帮
    助她呢？
"""
"""
输入描述
    输入的第一行有两个正整数n,m，分别表示字符串的长度和询问的个数。
    接下来一行是一个长为n的字符串。字符串中仅有小写英文字母。
    接下来m行，每行有四个数a,b,c,d，表示询问s[a...b]的所有子串和s[c...d]的最长公共前缀的最大值。

    数据范围：对于所有的数据，1≤n, m≤100000, a≤b, c≤d, 1≤a,b,c,d≤n
"""
"""
输出描述
    对于每一次询问，输出答案。
"""
line1 = []
line1 = [int(n) for n in input().split()]
line2 = input()
s = line2
length = line1[0]
times = line1[1]
while times > 0:
    times = times - 1
    line3 = []
    line3 = [int(n) for n in input().split()]
    a = line3[0] - 1
    b = line3[1] - 1
    c = line3[2] - 1
    d = line3[3] - 1
    s1 = s[a:b + 1]
    s2 = s[c:d + 1]
#     先将s1、s2的字串全部找到，放到两个列表里
    substr1 = []
    substr2 = []
    for e in range(len(s1)):
        substr1 = substr1 + [s1[:e + 1]]
    for f in range(len(s2)):
        substr2 = substr2 + [s2[:f + 1]]
#     再在这两个放满了前缀的列表里找到最长的公共前缀
    longest = ""
    for item1 in substr1:
        for item2 in substr2:
            if item1 == item2 and len(item1) >= len(longest):
                longest = item1
    print(len(longest))