"""
2.23
多数元素
使用set函数取出数组中的重复元素
然后使用count函数计算每个元素在原数组中的个数
"""
inp = list(map(int, input().split(",")))
length = len(inp)
require = length//2
li = list(set(inp))
for i in li:
    if inp.count(i) > require:
        print(i)
