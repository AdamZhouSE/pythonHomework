stones = input().split(",")
stones = list(map(int, stones))
stones = sorted(stones)
n = len(stones)
space = stones[n - 1] - stones[0] + 1 - n
if stones[n - 1] - stones[n - 2] < stones[1] - stones[0]:
    maxstep = space - (stones[n - 1] - stones[n - 2] - 1)
else:
    maxstep = space - (stones[1] - stones[0] - 1)
minstep = maxstep
i =1
for j in range(n):
    while stones[j]-stones[i]>=n:
        i += 1
    if j-i+1 == n-1 and stones[j]-stones[i]==n-2:
        minstep = min(2,minstep)
    else:
        minstep = min(minstep,n-(j-i+1))
result = []
result.append(minstep)
result.append(maxstep)
print(result)