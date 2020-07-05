n = eval(input())
a = [int(x) for x in input().split()]
m = eval(input())
q = [int(x) for x in input().split()]
beginBook = [0] * (n + 1)
endBook = [0] * (n + 1)
beginBook[0] = 1
endBook[0] = beginBook[0] + a[0] - 1
for i in range(1, n):
    beginBook[i] = beginBook[i - 1] + a[i - 1]
    endBook[i] = beginBook[i] + a[i] - 1
for i in range(m):
    j = 0
    while not (beginBook[j] <= q[i] <= endBook[j]):
        j += 1
    print(j+1)