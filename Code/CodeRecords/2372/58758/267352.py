T = int(input())
ans = 0
res = []
for i in range(0, T):
    N, X, Y = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    sub = []
    for j in range(0, len(A)):
        sub.append([A[j]-B[j], A[j], B[j]])
    sub.sort()
    ind = 0
    while ind < len(sub):
        if sub[ind][0] < 0:
            ind += 1
        else:
            break
    for k in range(0, Y):
        ans += sub[k][2]
    for k in range(len(sub)-X, len(sub)):
        ans += sub[k][1]
    cover = X+Y-N
    for k in range(Y-cover, Y):
        if sub[k][1] > sub[k][2]:
            ans -= sub[k][2]
        else:
            ans -= sub[k][1]
    res.append(ans)
    ans = 0
for i in res:
    print(i)
