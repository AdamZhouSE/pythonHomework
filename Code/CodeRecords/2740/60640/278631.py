inp = eval(input())
times = []
for c in inp:
    time = int(c[:2])*60 + int(c[3:])
    if time in times:
        print(0)
        exit()
    times.append(time)
times.sort()
times.append(times[0]+1440)
ans = min(times[i]-times[i-1] for i in range(1, len(times)))
print(ans)
