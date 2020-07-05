n = int(input())
time = sorted(list(set(map(int, input().split(' ')))))
satisfied = [time[0]]
for i in range(1, len(time)):
    wait = sum(satisfied[:i])
    for j in range(i, len(time)):
        if time[j] >= wait:
            satisfied.append(time[j])
            break
print(len(satisfied))
