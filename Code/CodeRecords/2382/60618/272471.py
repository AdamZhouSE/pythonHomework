n=int(input())
ab=[[0]*2]*n
for i in range(0,n):
    ab[i] = [int(k) for k in input().split()]
for j in range(0,n):
    for k in range(0,n):
        if ab[j][1]>=ab[k][0] and ab[j][0]<ab[k][1]:
            ab[j]=[min(ab[j][0],ab[k][0]),max(ab[j][1],ab[k][1])]
            ab[k]=ab[j]
re=list(set([tuple(t) for t in ab]))
for i in range(1,len(re)):
    for j in range(0,len(re)-i):
        if re[j][0]>re[j+1][0]:
            re[j],re[j+1]=re[j+1],re[j]
for i in range(0,len(re)):
    string=str(re[i][0])+' '+str(re[i][1])
    print(string)

            
    