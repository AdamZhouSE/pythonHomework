"""
O(N)
"""
t = int(input())
for i in range(t):
    inp = list(input())
    set_inp = list(set(inp))
    if len(set_inp) == len(inp):
        print(-1)
    else:
        MAX_CHAR = 256
        # 记录每个字符的位置，-1表示从未出现过
        firstIndex = [-1 for x in range(MAX_CHAR)]
        res = 0
        for j in range(len(inp)):
            # 字符的位置
            start = firstIndex[ord(inp[j])]
            # 字符第一次出现，更新其位置
            if start == -1:
                firstIndex[ord(inp[j])] = j
            # 字符再次出现，此时的位置是j，减掉原来存储的位置start，获取中间字符长度
            else:
                res = max(res, abs(j-start-1))
        print(res)
