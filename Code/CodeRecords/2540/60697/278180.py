import sys
t=list(map(int,input().split(' ')))
K=t[0]
N=t[1]
C=t[2]
res=[]
for i in range(K):
    res.append(list(map(int,input().split(' '))))
start=[]
end=[]
nums=[]
res.sort(key=lambda x:(x[1],x[0]))

for i in range(K):
    start.append(res[i][0])
    end.append(res[i][1])
    nums.append(res[i][2])
b=[0 for i in range(20000000)]
ans=0

for i in range(K):
    Min = sys.maxsize
    if(b[start[i]]<C):
        for j in range(start[i],end[i]):
            Min=min(C-b[j],Min)
            if(Min==0):
                break
        if(Min!=0):
            if(Min>=nums[i]):
                for j in range(start[i],end[i]):
                    b[j]+=nums[i]
                ans+=nums[i]
            else:
                for j in range(start[i],end[i]):
                    b[j]+=Min
                ans+=Min
print(ans)

