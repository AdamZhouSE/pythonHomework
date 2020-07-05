t = int(input())
for ti in range(t):
    s = input()
    le = 0
    ri = 0
    co=0
    for j in s:
        if j=='(':
            le=le+1
        if j==')' and le>0:
            le=le-1
            co=co+1
    print(2*co)