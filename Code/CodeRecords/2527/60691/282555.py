s = input()
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())

count = 0
for i in range(len(s)):
    if s[i] == '[':
        count += 1
count -= 1

l = [[] for i in range(count)]

s = s.replace('[', '')
s = s.replace(']', '')
l1 = s.split(',')

for i in range(count):
    for j in range(len(l1) // count):
        l[i].append(int(l1[(len(l1) // count) * i + j]))

# 过滤
removelist = []

if veganFriendly:
    for i in range(len(l)):
        if l[i][2] == 0 or l[i][3] > maxPrice or l[i][4] > maxDistance:
            removelist.append(l[i])
else:
    for i in range(len(l)):
        if l[i][3] > maxPrice or l[i][4] > maxDistance:
            removelist.append(l[i])

for i in range(len(removelist)):
    l.remove(removelist[i])

# 排序
l = sorted(l, key=lambda x: (x[1], x[0]), reverse=True)

nums = []
for i in range(len(l)):
    nums.append(l[i][0])

print(nums)