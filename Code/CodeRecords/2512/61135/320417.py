reqlist = input().split(" ")
nums = int(reqlist[0])
P = int(reqlist[1]);
numslist = input().split(" ")
numslist = list(int(x) for x in numslist)
times = int(input())
result=[]
for i in range(times):
    req = input().split(" ")
    req = list(int(x) for x in req)
    type=req[0]
    if(type==1):
        l=req[1]-1
        r=req[2]
        for j in range(l,r):
            numslist[j]=numslist[j]*req[3]
    if(type==2):
        l=req[1]-1
        r=req[2]
        for j in range(l,r):
            numslist[j]=numslist[j]+req[3]
    if(type==3):
        l=req[1]-1
        r=req[2]
        ans=0
        for j in range(l,r):
            ans+=numslist[j]
        result.append(str(ans%P))
for i in result:
    print(i)