result=0
nums=input().split(" ")
n=int(nums[0])
m=int(nums[1])
corral=[]
have=[]
for i in range(n):
    corral.append(int(input()))
    have.append(0)
ls=[]
no=0
for i in range(m):
    ls.append(input().split(" "))
    ls[i]=[int(x) for x in ls[i]]
for i in range(m):
    L=ls[i][0]-1
    R=ls[i][1]-1
    can=True
    for j in range(L,R+1):
        if have[j]+1>corral[j]:
            can=False
            break
    if can:
        for j in range(L, R + 1):
            have[j]=have[j]+1
    else:
        no=no+1
result=m-no
print(result)

