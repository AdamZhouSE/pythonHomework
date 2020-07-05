# 5
# -1
# 1
# 2
# 1
# -1
size=int(input())
nums=[]
for i in range(size):
    nums.append(int(input()))
nums.insert(0,0)
res=0
maxchain=0
for i in range(1,size+1):
    res=0
    k=i
    while k!=-1:
        k=nums[k]
        res=res+1
    if(res>maxchain):
        maxchain=res
print(maxchain)
