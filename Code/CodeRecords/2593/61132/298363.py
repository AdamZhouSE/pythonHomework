def bala(l):
    le=len(l)
    for i in range(le):
        for j in range(i+1,le):
            for k in range(j+1,le):
                for r in range(k+1,le):
                    if l[i]+l[j]==l[k]+l[r]:
                        return ' '.join(map(str,[i,j,k,r]))
    else:
        return "no pairs"

t = int(input())
for j in range(t):
    k = int(input())
    l = list(map(int, input().split()))
    print(bala(l))