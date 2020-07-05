n=int(input())
qus=[]
for i in range(0,n):
    qus.append(list(map(int,input().split())))
qus=sorted(qus,key=lambda x:(x[0],x[1]))
l=qus[0][0]
r=qus[0][1]
ans=[]
for i in range(1,n):
    if qus[i][0]>r:
        ans.append([l,r])
        l=qus[i][0]
        r=qus[i][1]
    else:
        r=qus[i][1]
ans.append([l,r])
for i in range(0,len(ans)):
    print(str(ans[i][0])+' '+str(ans[i][1]))