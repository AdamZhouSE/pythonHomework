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
print(numbers)