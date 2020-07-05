nums=eval(input())
result=[]
for item in nums:
    if item%2==0:
        result.append(item)
for item in nums:
    if item%2==1:
        result.append(item)
print(result)