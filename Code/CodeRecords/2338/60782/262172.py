"""
题目描述
    给定一个由N个正整数和另一个数字X组成的数组A。确定A中是否存在两个元素的总和恰好为X。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。每个测试用例的第一行是N和X，N是数组的大小。
    每个测试用例的第二行包含代表数组元素A [i]的N个整数。
"""
"""
输出描述
    如果A中存在两个元素的总和恰好为X，则打印“Yes”，否则为“No”（不带引号）。
"""

times = int(input())
while times > 0:
    times = times - 1
    line1 = list(map(int, input().split(" ")))
    line2 = list(map(int, input().split(" ")))
    yes = False
    for i in range(line1[0]):
        for j in range(line1[0]):
            if i != j:
                if line2[i] + line2[j] == line1[1]:
                    yes = True
                    break
    if yes:
        print("Yes")
    else:
        print("No")