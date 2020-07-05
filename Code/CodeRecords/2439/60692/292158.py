from collections import defaultdict
node = defaultdict(int)
n = int(input())
ans = []
weight = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n - 1):
    a_b_w = input().split(" ")
    a = int(a_b_w[0])
    b = int(a_b_w[1])
    w = int(a_b_w[2])
    weight[a][b] = w
    node[a] = b
m = int(input())
for i in range(m):
    res = 0
    s_e = input().split(" ")
    s = int(s_e[0])
    e = int(s_e[1])
    if s == e:
        ans.append(0)
    else:
        end = node[s]
        while end != e:
            res = res ^ weight[s][end]
            s = end
            end = node[s]
        ans.append(res ^ weight[s][end])
for i in ans:
    print(i)