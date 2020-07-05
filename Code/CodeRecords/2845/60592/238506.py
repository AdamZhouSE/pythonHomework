total = int(input())
res = []
has = 0
for i in range(0,total):
    ls = list(map(int,input().split()))
    res.append(ls)
for i in range(0,total):
    for j in range(0,total):
        if res[i][0] < res[j][0] and res[i][1] > res[j][1]:
            has = 1
            break
    if has:
        break
if has:
    print("Happy Alex")
else:
    print('Poor Alex')