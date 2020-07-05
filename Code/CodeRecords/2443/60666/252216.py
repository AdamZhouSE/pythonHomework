nums=input()
nums=nums[1:-1]
numbers=[]
for x in nums:
    if x.isdigit():
        numbers.append(int(x))
    else:
        continue
numbers.sort()
numbers.reverse()
s=""
for i in numbers:
    s+=str(i)
print(s)