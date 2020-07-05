input()
stations = list(map(int, input().split(" ")))
temp1 = list(map(int, input().split(" ")))
source = temp1[0]
dest = temp1[1]
if source > dest:
    source, dest = dest, source
temp2 = dest - source
start = source - 1
sum0 = sum(stations)
sum1 = 0
for i in range(0, temp2):
    sum1 += stations[start+i]
sum2 = sum0 - sum1
print(min(sum1, sum2))