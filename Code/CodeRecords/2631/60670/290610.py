n,g=map(int,input().split())
change=[]
for i in range(0,n):
    change.append(list(map(int,input().split())))
change=sorted(change,key=lambda x:x[1])
cowNo={}
num=0
for i in range(0,n):
    if not change[i][1] in cowNo:
        cowNo[change[i][1]]=num
        num+=1#为牛重新编号，从0开始
change=sorted(change,key=lambda x:x[0])
maxg=g
maxn=999999999
cowg=[g for i in range(0,num)]
cnt=0
for i in range(0,n):
    if change[i][2]>0:
        cowg[cowNo[change[i][1]]]+=change[i][2]
        if cowg[cowNo[change[i][1]]]>maxg:
            maxg=cowg[cowNo[change[i][1]]]
            maxn=1
            cnt+=1
        elif cowg[cowNo[change[i][1]]]==maxg:
            maxn+=1
            cnt+=1
    elif change[i][2]<0:
        if cowg[cowNo[change[i][1]]]==maxg:
            cowg[cowNo[change[i][1]]]+=change[i][2]
            if maxn>1:
                maxn-=1
            else:
                tmp=0
                tmax=0
                for j in range(0,num):
                    if cowg[j]==tmax:
                        tmp+=1
                    if cowg[j]>tmax:
                        tmax=cowg[j]
                        tmp=1
                        if tmax==g:
                            tmp=999999999
                maxg=tmax
                maxn=tmp
            cnt+=1
        else:
            cowg[cowNo[change[i][1]]]+=change[i][2]
print(cnt)