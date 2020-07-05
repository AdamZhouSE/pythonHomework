def D2G(x):
    return x^(x>>1)

ans = []
n = int(input())
start = int(input())
tag = 0
index = 0
length = (1<<n) - 1
G = [0] * (length+1)
for i in range(length+1):
    G[i] = D2G(i)
    if start == G[i]:
        tag = i
while index <= length:
    ans.append(int(G[tag]))
    tag = (tag+1)%(length+1)
    index += 1
print(ans)
