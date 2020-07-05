nums=input()
nums=nums[1:-1]
numbers=[]
for x in nums:
    if x.isdigit():
        numbers.append(int(x))
    else:
        continue
numbers.sort()
integers=[]
for i in range(len(numbers)):
    integers.append(i)
for element in numbers:
    if element not in integers:
        result=element
        break
print(result)