def DG(x):
    return x^(x>>1)


n = int(input())
start = int(input())
tag = 0
index = 0
length = (1<<n) -1
g = [0]*(length+1)
for i in range(length+1):
    g[i] = DG(i)
    if start == g[i]:
        tag = i
ans = []
while index <= length:
    ans.append(g[tag])
    tag = (tag+1) % (length+1)
    index+=1
print(ans)