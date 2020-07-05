import math
buckets=int(input())
minutesToDie=int(input())
minutesToTest=int(input())
states = minutesToTest // minutesToDie + 1
num=math.ceil(math.log(buckets) / math.log(states))
print(num)