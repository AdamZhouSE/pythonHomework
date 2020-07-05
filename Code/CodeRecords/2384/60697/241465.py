a=int(input())
sizes=[]
nums=[]
tmp=[]
for i in range(a):
    sizes.append(int(input()))
    nums.append(list(map(int,input().split(' '))))
for i in range(a):
    tmp=[]
    for j in nums[i]:
        if(j>0):
            tmp.append(j)
    tmp.sort()
    s=0
    if(tmp[0]==1):
        for k in range(len(tmp)-1):
            if(tmp[k+1]-tmp[k]>1):
                s=tmp[k]+1
                break
    else:
        s=1
    if(s==0):
        s=tmp[len(tmp)-1]+1
    print(s)