n,m=map(int,input().split())
num=[[] for i in range(0,n)]
kind=0
for step in range(0,m):
    q,l,r=map(int,input().split())
    if q==1:
        for i in range(l-1,r):
            num[i].append(kind)
        kind+=1
    else:
        re=[]
        for i in range(l-1,r):
            for j in range(0,len(num[i])):
                if not num[i][j] in re:
                    re.append(num[i][j])
        print(len(re))