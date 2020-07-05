nums = list(map(int, input().strip('[]').split(',')))
m = 0
r = []

for i in nums:
    if nums.count(i) > m:
        m = nums.count(i)
        r.append(i)
for i in nums:
    if nums.count(i) == m and i not in r:
        m = nums.count(i)
        r.append(i)


print(r)