import itertools
numbers=list(map(int,input().split(",")))
n=numbers[1]
k=numbers[0]
nums=[1,2,3,4,5,6,7,8,9]
res=[]
for p in itertools.combinations(nums,k):
    sum=0
    for num in p:
        sum=sum+num
    if sum==n:
        result=[]
        for num in p:
            result.append(num)
        res.append(result)
print(res)