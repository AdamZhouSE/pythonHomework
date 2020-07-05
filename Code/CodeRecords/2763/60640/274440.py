"""
有两种情况
1. 序列最后到达m，那么n-1个元素都不大于m/2，递归m/2 n-1
2. 序列最后没有到达m，那么递归m-1 n
"""


def get_number_of_sequences(m, n):
    if m < n:
        return 0
    if n == 0:
        return 1
    res = (get_number_of_sequences(m-1, n) + get_number_of_sequences(m//2, n-1))
    return res


t = int(input())
for i in range(t):
    inp = input().split(" ")
    M, N = int(inp[0]), int(inp[1])
    print(get_number_of_sequences(M, N))
