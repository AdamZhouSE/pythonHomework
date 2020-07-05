# 2
# 5
# 5 5 4 6 4
# 5
# 9 9 9 2 5
a=int(input())
sizes=[]
nums=[]
for i in range(a):
    sizes.append(int(input()))
    nums.append(list(map(int,input().split(' '))))
tmp={}
res=[]
tmpa=[]
for i in range(a):
    tmp={}
    tmpa=[]
    for j in range(sizes[i]):
        if(nums[i][j] in tmp.keys()):
            tmp[nums[i][j]]=tmp[nums[i][j]]+1
        else:
            tmp[nums[i][j]]=1
    tmp=sorted(tmp.items(),key=lambda item:(item[1],-item[0]),reverse=True)
    for k in range(len(tmp)):
        for l in range(tmp[k][1]):
            tmpa.append(tmp[k][0])
    res.append(tmpa)
s=""
for i in range(len(res)):
    print(" ".join(list(map(str,res[i])))+" ")





