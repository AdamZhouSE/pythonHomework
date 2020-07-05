t = int(input())
for i in range(0, t):
    n = int(input())
    total = 0
    for j in range(1, n+1):
        total += j**5
    print(total)
