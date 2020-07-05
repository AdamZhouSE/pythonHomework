n = int(input())
k = int(n / 2)
for i in range(0,k):
    s = 'D' * (2 * i + 1)
    s = '*' * (k - i) + s + '*' * (k - i)
    print(s)
for i in range(k,-1,-1):
    s = 'D' * (2 * i + 1)
    s = '*' * (k - i) + s + '*' * (k - i)
    print(s)