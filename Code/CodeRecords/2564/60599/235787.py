s = input()
s = s[1:len(s) - 1]
s = list(map(int, s.split(',')))

k = int(input())  # 几个数
x = int(input())  # 接近几

index = 0  # 得到索引
for i in range(len(s)):
    if (s[i] == x):
        index = i

nums = []
d = 0

flag1 = 0
flag2 = 0

for i in range(k):
    if flag1 == 1:
        d = d - 1
        nums.append(s[index + d])
        continue
    if flag2 == 1:
        d = d + 1
        nums.append(s[index + d])
        continue
    nums.append(s[index + d])
    if (d < 0):
        d = -d
        if (index + d > len(s) - 1):
            d = -d
            flag1 = 1
    elif (d > 0):
        d = -(d + 1)
        if (index + d < 0):
            d = -d - 1
            flag2 = 1
    if (d == 0 and index!=0): d = d - 1
    if (d==0 and index==0):flag2=1

nums.sort()
print(nums)
