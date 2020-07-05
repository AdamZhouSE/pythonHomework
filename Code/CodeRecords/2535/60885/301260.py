nums = eval(input())
n = len(nums)
group = [i for i in range(n)]

for i in range(n):
    num = nums[i]
    if i < num:
        l,r = i,num+1
    else:
        l,r = num+1,i

    carry = []
    for j in range(l,r):
        carry.append(group[j])
        group[j] = num
    for j in range(n):
        if group[j] in carry:
            group[j] = num
print(len(set(group)))
        
