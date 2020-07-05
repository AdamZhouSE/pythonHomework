nums=list(map(int,input()[1:-1].split(",")))
s=set(nums)
result=[]
for i in s:
    if nums.count(i)>len(nums)/3:
        result.append(i)
print(result)