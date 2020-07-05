"""
使用1个n+1的数组
分别计算3，5，10到n可能的移动
"""


def nums(n):
    table = [0 for x in range(n+1)]
    table[0] = 1
    for i in range(3, n+1):
        table[i] += table[i-3]
    for i in range(5, n+1):
        table[i] += table[i-5]
    for i in range(10, n+1):
        table[i] += table[i-10]
    return table[n]


t = int(input())
for k in range(t):
    inp = int(input())
    ans = nums(inp)
    print(ans)
