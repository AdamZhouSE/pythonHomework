num = int(input())
n = list(map(int, input().split()))
tmp = 1
maxnum = 1
for i in range(num-1):
    if n[i] < n[i + 1] and i != num-1:
        tmp = tmp + 1
    else:
        tmp = 1
        if tmp >= maxnum:
            maxnum = tmp
print(maxnum)
