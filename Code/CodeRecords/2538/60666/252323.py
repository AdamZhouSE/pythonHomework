nums=input()
nums=nums[1:-1]
numbers=[]
for x in nums:
    try:
        num=int(x)
        if isinstance(num,int):
            numbers.append(int(x))
    except:
        continue
numbers.sort()
if len(numbers) == 0:
    print(1)
else:
    for i in range(len(numbers)):
        p=i
        while numbers[p]>0 and numbers[p]<=len(numbers) and numbers[p]!=p+1:
            t=numbers[p]
            numbers[p],numbers[t-1]=numbers[t-1],numbers[p]
            if numbers[p]==t:
                break
    for i in range(len(numbers)):
        if numbers[i]!=i+1:
            result=i+1
    if result==i+1:
        print(result)
    result=len(nums)+1
    print(result)