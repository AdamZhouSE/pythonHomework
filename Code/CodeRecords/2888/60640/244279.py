"""
2.20
Eugeny的数组
要使得范围内为0
1. 范围内有偶数个数，即r-l+1为偶数
2. 分别需要1和-1的数量为(r-l+1)/2
"""
inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
data = list(map(int, input().split(" ")))
num_one = data.count(1)
num_neg = data.count(-1)
for i in range(0, m):
    limit = input().split(" ")
    l, r = int(limit[0]), int(limit[1])
    ant = (r - l + 1) // 2
    if (r - l + 1) % 2 == 0 and num_neg >= ant and num_one >= ant:
        print(1)
    else:
        print(0)
