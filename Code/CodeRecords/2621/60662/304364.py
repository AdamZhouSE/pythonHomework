num = list(map(int,input().strip('[],').split(',')))
now = num[0]
sums = list()
sums.append(now)
for i in range(1,len(num)):
    sums.append(max(num[i], sums[i-1]+num[i]))

print(max(sums))