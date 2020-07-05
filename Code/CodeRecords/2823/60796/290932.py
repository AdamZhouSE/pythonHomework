def build(s):
    if len(s)==k:
        this[0]=this[0]+1
        return
    i=int(s[0])-1
    j=len(ls[i])-1
    while j>=0:
        build(str(ls[i][j])+s)
        j=j-1



result=0
nums=input().split(" ")
N=int(nums[0])
k=int(nums[1])
ls=[]
for i in range(1,N+1):
    s=[]
    for j in range(1,i+1):
        if i%j==0:
            s.append(j)
    ls.append(s)

for i in range(len(ls)):
    #最大元素是i+1
    this=[0]
    build(str(i+1))
    result=result+this[0]

print(result)



