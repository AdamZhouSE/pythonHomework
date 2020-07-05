n = int(input())
time = sorted(list(map(int, input().split(' '))))
count = 1
for i in range(1, n):
    if sum(time[:i]) <= time[i]:
        count += 1
print(count)