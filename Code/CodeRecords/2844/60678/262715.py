nANDt = input().split()
n = int(nANDt[0])
t = int(nANDt[1])
plans = input().split()
for i in range(0, n):
    plans[i] = int(plans[i])

readed = []
for i in range(0, n):
    count = 0
    timeAcumlated = 0
    for j in range(i, n):
        timeAcumlated += plans[j]
        if timeAcumlated > t:
            break
        count += 1
    readed.append(count)
readed.sort(reverse=True)
print(readed[0])