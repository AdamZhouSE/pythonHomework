nums=list(map(int,input()[1:-1].split(",")))
numset=list(set(nums))
ans=[]
for num in numset:
    if nums.count(num)>len(nums)//3:
        ans.append(num)
print(ans)