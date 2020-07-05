nums=eval(input())
res=[]
for n in nums:
    if nums.count(n)>len(nums)//3:
        res.append(n)
print(list(set(res)))#用集合方式去除重复值后再转为列表