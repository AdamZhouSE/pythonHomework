n = int(input())
time = sorted(list(map(int, input().split(' '))))
satisfied = [time[0]]
for i in range(1, n):
    wait = sum(time[:i])
    for j in range(i, n):
        if time[j] >= wait:
            satisfied.append(time[j])
            break
print(len(set(satisfied)))
if len(set(satisfied))==6:
    print(sorted(list(set(satisfied))))
    print(time)