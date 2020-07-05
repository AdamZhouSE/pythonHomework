str1 = input().split()
n = int(str1[0])
m = int(str1[1])
nums = input().split()
count_m1 = 0
count1 = 0
for x in nums:
    if x == "-1":
        count_m1 += 1
    else:
        count1 += 1
for x in range(m):
    str2 = input().split()
    l = int(str2[0])
    r = int(str2[1])
    if r == l or (r - l + 1) % 2 != 0 or (r - l + 1) // 2 > count1 or (r - l + 1) // 2 > count_m1:
        print(0)
    else:
        print(1)
