nums=input()
nums=nums[1:-1]
numbers=[]
for x in nums:
    if x.isdigit():
        numbers.append(int(x))
    else:
        continue
count=0
left=0
right=1
for i in range(len(numbers)):
    if  max(numbers[left:right])==right-1:
        left=right
        count+=1
    right+=1
print(count)