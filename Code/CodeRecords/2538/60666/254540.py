nums=eval(input())
nums.sort()
i=1
while True:
    if i in nums:
        i+=1
        continue
    else:
        result=i
        break
print(result)