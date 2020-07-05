n = int(input())
nums = input().split()
maxcount = 1
dic = {}
for x in nums:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
        if dic[x] > maxcount:
            maxcount = dic[x]
print(maxcount)
