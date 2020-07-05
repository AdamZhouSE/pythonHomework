"""
最后剩5根给对手就获胜
推广：
剩5n给对手
"""
t = int(input())
for i in range(t):
    n = int(input())
    if n % 5 == 0:
        print(-1)
    else:
        res = 0
        for j in range(1, 5):
            if (n-j) % 5 == 0:
                res = j
                break
        print(res)
