import math

buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
time = math.floor(minutesToTest / minutesToDie)
time_valid = time + 1
i = 0
while pow(time_valid, i) < buckets:
    i = i + 1
print(i)