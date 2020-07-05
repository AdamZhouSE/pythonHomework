n,m=map(int,input().split())
message=[]
stu=[1]*n
for i in range(0,m):
    message.append(int(input()))
    if stu[i-1]==1:
        stu[i-1]=0
    else:
        stu[i-1]=1
    loca=[]
    re=0
    count=0
    first=0
    last=0
    for j in range(0,n):
        if stu[j]==0:
            loca.append(j)
    for j in range(0,len(loca)):
        for k in range(j,len(loca)):
            if loca[k]-loca[j]==(2k-2j):
                count+=1
                if k-j>count:
                    count=k-j
                    first=j
                    last=k
    if first!=0 and last!=len(loca)-1:
        if loca[first]-loca[first-1]>1 and loca[last+1]-loca[last]>1:
            print(2*last-2*first+3)
        
            