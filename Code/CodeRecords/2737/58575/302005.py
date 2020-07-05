nums=input()[1:-1].split(",")
n=len(nums)
res={}
result=[]
target=n//3
for i in nums:
    if i in res:
        res[i]+=1
        if res[i]>=target:
            result.append(i)
    else:
        res[i]=0
result=list(map(int,result))
print(result)