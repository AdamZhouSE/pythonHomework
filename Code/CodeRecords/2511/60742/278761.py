n,s = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    maxK = 0
    while maxK*2+i-1<n:
        sum1 = 0
        sum2 = 0
        for j in range(i,i+maxK):
            sum1 += a[j]
        if sum1>s:
            break
        for j in range(i+maxK,i+2*maxK):
            sum2 += a[j]
        if sum2>s:
            break
        maxK += 1
    maxK -= 1
    print(2*maxK)