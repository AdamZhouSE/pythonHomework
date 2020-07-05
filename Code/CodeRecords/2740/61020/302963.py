import math

import itertools

times = input()[1:-1].split(',')
for j in range(len(times)):
    times[j] = times[j][1:-1]
    times[j] = (int(times[j].split(':')[0]), int(times[j].split(':')[1]))

times_in_min = []
for t in times:
    times_in_min.append(t[0] * 60 + t[1])

pairs_of_times_in_min = list(itertools.combinations(times_in_min, 2))
time_diff = []

for pair in pairs_of_times_in_min:
    time_diff.append(min(int(math.fabs(pair[0] - pair[1])), int(math.fabs(1440 - int(math.fabs(pair[0] - pair[1]))))))

print(min(time_diff))

# print(int(math.fabs(-3)))
