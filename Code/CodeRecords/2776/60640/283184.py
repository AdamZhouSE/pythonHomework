"""
连接词
深度优先搜索
"""


def dfs(s, list_str, depth, index):
    if index == len(s):
        return depth > 1
    for i in range(index+1, len(s)+1):
        if s[index:i] in list_str:
            if dfs(s, list_str, depth+1, i):
                return True


inp = eval(input())
res = []
for string in inp:
    if dfs(string, inp, 0, 0):
        res.append(string)
print(res)
