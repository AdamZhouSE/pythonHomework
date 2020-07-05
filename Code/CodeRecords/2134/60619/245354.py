import math
buckets = int(input())
deathTime = int(input())
testTime = int(input())
test = int(testTime/deathTime)
result = math.ceil(pow(buckets, 1/test))
print(result-1)