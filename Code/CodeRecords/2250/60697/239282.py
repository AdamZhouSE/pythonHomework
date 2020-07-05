nums=[]
size=int(input())
for i in range(size):
    nums.append(list(map(int,input().split(','))))
res={}
res2={}
for j in range(0,size):
    for i in range(j+1,size):
        if((nums[j][1] - nums[i][1])!=0):
            a=(nums[j][0] - nums[i][0])/(nums[j][1] - nums[i][1])
            if a not in res.keys():
                res[a]=1
            else:
                res[a]=res[a]+1
        else:
            a =nums[i][1]
            if a not in res.keys():
                res[a] = 1
            else:
                res[a] = res[a] + 1
maxsize=0
for i in res.keys():
    if(res[i]>maxsize):
        maxsize=res[i]
for i in res2.keys():
    if(res2[i]>maxsize):
        maxsize=res2[i]
k=0
while k*(k-1)<maxsize*2:
    k=k+1
print(k)