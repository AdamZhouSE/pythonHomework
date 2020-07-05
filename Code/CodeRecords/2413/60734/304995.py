n = int(input())
start = int(input())
tag = 0
length = 2**n
g = [0]*length
for i in range(length):
    g[i] = i ^ (i>>1)
    if start == g[i]:
        tag = i
ans = []
for i in range(length):
    ans.append(g[tag])
    tag = (tag+1)%length
print(ans)