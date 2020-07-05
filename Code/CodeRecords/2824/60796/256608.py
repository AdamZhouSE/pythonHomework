nums=input().split(" ")
n=int(nums[0])#囚犯数
t=int(nums[1])#犯罪水平
c=int(nums[2])#选择的囚犯数
ls=input().split(" ")
ls=[int(x) for x in ls]
result=0
for i in range(n):
    j=i+c
    if j<=n:
        subls=ls[i:j]
        yes=1
        for a in range(len(subls)):
            if subls[a]>t:
                yes=0
                break
        if yes==1:
            result=result+1

print(result)

