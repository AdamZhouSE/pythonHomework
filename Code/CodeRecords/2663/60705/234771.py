# 当n=1时，res = 1+2 = 3
# 当n=2时，res = 1+2+3+4 = 10
# 当n=3时，res = 1+2+3+4+5+6 = 21
line = int(input())
for i in range(0, line):
    n = int(input())
    res = 0
    for j in range(1, 2*n+1):
        res += j
    print(res)
