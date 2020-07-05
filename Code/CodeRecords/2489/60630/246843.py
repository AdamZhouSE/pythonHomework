num = [int(i) for i in input("")[1 : -1].split(',')]
n = len(num)
lower = int(input("")) ; upper = int(input("")) + 1

aSum = [0]
for i in range(0, n) :
    aSum.append(aSum[i] + num[i])
ans = 0
for i in range(0, n) :
    for j in range (i + 1, n + 1) :
        if (aSum[j] - aSum[i]) in range(lower, upper) :
            ans += 1

print(ans)
