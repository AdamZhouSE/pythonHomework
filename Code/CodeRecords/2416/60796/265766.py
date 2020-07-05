def longest(ls):
    r=[]
    for i in range(len(ls)-1):
        j=i+1
        this=1
        while j<len(ls):
            if ls[j]!=ls[j-1]:
                this=this+1
            else:
                break
            j=j+1
        r.append(this)

    return r

nums=input().split(" ")
student=int(nums[0])
M=int(nums[1])
ls=[]
for i in range(student):
    ls.append(1)
instruct=[]
for i in range(M):
    instruct.append(int(input())-1)
result=[]

for i in range(len(instruct)):
    if ls[instruct[i]]==1:
        ls[instruct[i]]=0
    else:
        ls[instruct[i]]=1
    result.append(max(longest(ls)))
for i in range(len(result)):
    print(result[i])


