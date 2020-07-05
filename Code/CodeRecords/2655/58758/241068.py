count = int(input())
ans = []
for i in range(0, count):
    N = int(input())
    target = 1
    while True:
        if target >= N:
            ans.append(target)
            break
        else:
            target *= 2
for j in ans:
    print(j)
