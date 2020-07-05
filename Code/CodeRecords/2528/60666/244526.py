nums=input()
nums=nums[1:-1]
numbers=[]
for x in nums:
    if x.isdigit():
        numbers.append(int(x))
    else:
        continue
numbers.sort()
print(numbers)