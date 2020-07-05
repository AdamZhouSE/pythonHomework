def countLuckyNum(string):
    count = 0
    for i in string:
        if i == '4' or i == '7':
            count += 1
    return count


nANDk = input().split()
n = int(nANDk[0])
k = int(nANDk[1])
nums =input().split()
count = 0
for i in nums:
    if countLuckyNum(i) <= k:
        count += 1
print(count)