T = int(input())
res = [0 for _ in range(100)]
res[2] = 3
res[3] = 5
for i in range(4, 100):
    res[i] = res[i-1]+res[i-2]
for _ in range(T):
    a = int(input())
    print(pow(2,a)-res[a])

