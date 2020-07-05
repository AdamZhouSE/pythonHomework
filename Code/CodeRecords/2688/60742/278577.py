t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    sum = int(input())
    res = 0
    for i in range(2**n):
        sumV = 0
        for j in range(n):
            if i%2==1:
                sumV += a[j]
            i = i//2
        if sumV==sum:
            res += 1
    print(res)