le = int(input())
nums = []
subs = []
ret = []
l = le
while l:
    nums.append(int(input()))
    l -= 1
subs.append(nums)
for i in range(le-1):
    for j in range(i+1, le):
        temp = nums[:]
        if temp[i]>temp[j]:
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
