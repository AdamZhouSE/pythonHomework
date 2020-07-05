s = input()
bads = input()
k = int(input())

n = len(s)

table = set()
bads_idx = []
for i in range(n):
    if bads[i] == '0':
        bads_idx.append(i)

if k > len(bads_idx):
    k = len(bads_idx)
bads_idx = [-1] + bads_idx + [n]
for i in range(len(bads_idx)-1-k):
    l = bads_idx[i]
    r = bads_idx[i + k + 1]
    sub = s[l+1:r]
    for m in range(len(sub)):
        for n in range(m+1,len(sub)+1):
            table.add(sub[m:n])
print(len(table))