nums=eval(input())
minnum=min(nums)
i=min(minnum,1)
while i in nums or i<=0:
    i+=1
print(i)