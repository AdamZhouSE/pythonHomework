n = int(input())
time = sorted(list(map(int, input().split(' '))))
satisfied = [time[0]]
for i in range(1, n):
    wait = sum(time[:i])
    for j in range(1, n):
        if time[j] >= wait:
            satisfied.append(time[j])
            break
print(len(set(satisfied)))