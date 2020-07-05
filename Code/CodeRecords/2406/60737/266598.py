le = int(input())
nums = []
subs = []
ret = []
l = le
while l:
    nums.append(int(input()))
    l -= 1
subs.append(nums)
'''
for i in range(le-1):
    temp = nums[:]
    mini = temp[i+1]
    index = i+1
    for j in range(i+1, le):
        if temp[j]<mini:
            index = j
            mini = temp[j]
    t = temp[i]
    temp[i] = temp[index]
    temp[index] = t
    subs.append(temp)
    '''
temp = nums[:]
i = temp.index(max(temp))
j = temp.index(min(temp))
t = temp[i]
temp[i] = temp[j]
temp[j] = t
subs.append(temp)
for sub in subs:
    count = 0
    for i in range(le-1):
        for j in range(le-1):
            if sub[j]>sub[j+1]:
                a = sub[j]
                sub[j] = sub[j+1]
                sub[j+1] = a
                count += 1
    ret.append(count)
print(min(ret))
