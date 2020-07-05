a = [int(i) for i in input().split(',')]
a.sort()
n = len(a)
max_move = max(a[-1]-a[1],a[-2]-a[0])-n+2
min_move = max_move
i = 0
for j in range(n):
    while a[j]-a[i]+1>n:
        i += 1
    if j-i+1==n-1 and a[j]-a[i]==j-i:
        min_move = min(min_move,2)
    else:
        min_move = min(min_move,n-(j-i+1))
res = [min_move,max_move]
print(res)