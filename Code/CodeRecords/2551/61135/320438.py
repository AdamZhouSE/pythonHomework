reqlist = input().split(" ");
nums = int(reqlist[0])
P = int(reqlist[1])
numslist = [-1 for i in range(nums)]
result=[]
for i in range(P):
    req = input().split(" ")
    req = list(int(x) for x in req)
    type=req[0]
    if(type==0):
        l=req[1]-1
        r=req[2]
        for j in range(l,r):
            numslist[j]=- numslist[j]
    if(type==1):
        l=req[1]-1
        r=req[2]
        ans=0
        for j in range(l,r):
            if(numslist[j]==1):
                ans+=1
        print(str(ans))
