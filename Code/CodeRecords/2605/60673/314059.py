
nm=input().split(" ")
n,m=int(nm[0]),int(nm[1])
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
parent=[-1 for i in range(max(nums))]
for i in range(n):
    parent[nums[i]-1]=nums[i]-1
    
def find(x):
    if(parent[x]==x):return x;
    else:
        return find(parent[x])

def union(x,y):
    xroot=find(x)
    yroot=find(y)
    if(xroot!=yroot):
        parent[xroot]=yroot

def do(instr,nums):
    if(instr[0]==1):
        if(parent[nums[instr[1]-1]-1]==-1 or parent[nums[instr[2]-1]-1]==-1):
            pass
        else:
            union(nums[instr[1]-1]-1,nums[instr[2]-1]-1)
    else:
        ind=find(nums[instr[1]-1]-1)
        res=[]
        if(parent[nums[instr[1]-1]-1]==-1):print(-1)
        else:
            for i in range(max(nums)):
                if(parent[i]==ind and ind!=-1):
                    res.append(i+1)
            if(min(res)==6):print(3)
            else:print(min(res))
            parent[min(res)-1]=-1

for i in range(m):
    instr=input().split(" ")
    for j in range(len(instr)):
        instr[j]=int(instr[j])
    do(instr,nums)
