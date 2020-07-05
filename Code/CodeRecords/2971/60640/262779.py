"""
将字符串所有后缀与其后缀首字母的位置存入列表
排序输出位置
"""
inp = input()
lent = len(inp)
arr = []
for i in range(lent):
    suffix = inp[lent-i-1:lent]
    arr.append([suffix, lent-i])
arr.sort()
for i in range(lent):
    print(arr[i][1], end=" ")
