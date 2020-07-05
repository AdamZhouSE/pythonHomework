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
for i in range(1,len(numbers)+2):
    if i not in numbers:
        result=i
print(result)