def bala(l):
    le=len(l)
    for i in range(le):
        for j in range(le):
            if i == j: continue
            for k in range(le):
                if k == i or k == j: continue
                for r in range(le):
                    if r == i or r == j or r==k:continue
                    if l[i]+l[j]==l[k]+l[r]:
                        return ' '.join(map(str,[i,j,k,r]))
    else:
        return "no pairs"

t = int(input())
for j in range(t):
    k = int(input())
    s=input()
    if ',' in s:
        l=list(map(int,s.split(',')))
    else:
        l=list(map(int,s.split()))
    print(bala(l))