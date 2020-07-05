def toint(time):
    time = time.replace('"', "")
    time = time.split(":")
    time = int(time[0])*60 + int(time[1])
    return time


times = input()
times = times[1: len(times)-1].split(",")
n = len(times)
for i in range(n):
    times[i] = toint(times[i])
times.sort()
m = 24*60-(times[n-1]-times[0])
for i in range(1, n):
    m = min(m, times[i]-times[i-1])
print(m)