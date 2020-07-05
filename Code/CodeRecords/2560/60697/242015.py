# 2
# 6
# 2 2 1 3 3 3
# 3
# 8
# 2 4 1 5 3 5 1 3
# 2
a=int(input())
sizes=[]
nums=[]
M=[]

for i in range(a):
    sizes.append(int(input()))
    nums.append(list(map(int,input().split(' '))))
    M.append(int(input()))
for i in range(a):
    tmp = {}
    num=nums[i]
    size=sizes[i]
    m=M[i]
    for j in range(sizes[i]):
        if(nums[i][j] in tmp.keys()):
            tmp[nums[i][j]]=tmp[nums[i][j]]+1
        else:
            tmp[nums[i][j]]=1
    tmp = sorted(tmp.items(), key=lambda item: item[1])
    k=0
    for k in range(len(tmp)):
        m=m-tmp[k][1]
        if(m<0):
            break
        if(m==0):
            k=k+1
            break
    print(len(tmp)-k)
