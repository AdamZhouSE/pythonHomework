t=int(input())
for i in range(t):
    n,root=input().split()
    n=int(n)
    arr=list(map(str,input().split()))
    r=[]
    for j in range(n):
        r.append(input().split())
    result=[r[0][0]]
    for j in range(len(r)):
        for k in range(len(r[0])):
            if(r[j][k]=='1'):
                if(r[k-1][0] not in result):
                    result.append(r[k-1][0])
                    break
    print(*result)