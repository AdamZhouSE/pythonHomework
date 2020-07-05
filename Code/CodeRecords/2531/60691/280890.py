s = input()

l = []
for i in range(len(s)):
    l.append(s[i])
l.sort()

lelement = []
for i in range(len(l)):
    if not l[i] in lelement:
        lelement.append(l[i])

nums = []
for i in range(len(lelement)):
    nums.append(s.count(lelement[i]))

lresult = [[]for i in range(len(lelement))]

for i in range(len(lelement)):
    lresult[i].append(nums[i])
    lresult[i].append(lelement[i])

lresult.sort(reverse=True)

s = ''
for i in range(len(lresult)):
    for j in range(lresult[i][0]):
        s += lresult[i][1]

print(s)
