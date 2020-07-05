"""
2.19
删除重复元素
反转字符，保持顺序去除重复，再反转回来，能够保证最右边的剩余元素不变的
"""
n = int(input())
data = input().split(" ")
data.reverse()
res = list(set(data))
# 使得去除重复元素后顺序不变
res.sort(key=data.index)
res.reverse()
print(len(res))
for i in range(0, len(res)-1):
    print(res[i], end=" ")
print(res[len(res)-1])
