n = int(input())
steps = list(map(int, input().split(' ')))
print(steps.count(1))
counts = 1
ans = ''
for i in range(1, n):
    if steps[i] != 1:
        counts += 1
    else:
        ans += str(counts) + ' '
        counts = 1
print(ans + str(counts))
