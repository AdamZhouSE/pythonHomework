s = input()
count = 0

for i in range(len(s)):
    if s[i] == '[':
        count += 1
count -= 1

l = [[]for i in range(count)]

s = s.replace('[', '')
s = s.replace(']', '')
l1 = s.split(',')

for i in range(count):
    for j in range(len(l1) // count):
        l[i].append(int(l1[(len(l1) // count)*i+j]))

for i in range(len(l[0])-1):
    nums = []
    j = 0
    while 0+j <= len(l)-1 and i+j <= len(l[0])-1:
        nums.append(int(l[j][i+j]))
        j += 1

    nums.sort()
    for m in range(len(nums)):
        l[m][i+m] = nums[m]

for i in range(len(l)-1):
    nums = []
    j = 0
    while i+j <= len(l)-1 and 0+j <= len(l[0])-1:
        nums.append(int(l[i+j][j]))
        j += 1

    nums.sort()
    for m in range(len(nums)):
        l[i+m][m] = nums[m]

print(l)