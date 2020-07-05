"""
2.19
菲利亚的作业
用set去除重复
"""
n = int(input())
data = sorted(set(map(int, input().split(" "))))
if len(data) <= 2:
    print("YES")
elif len(data) == 3 and data[1] * 2 == data[0] + data[2]:
    print("YES")
else:
    print("NO")
