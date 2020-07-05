import math
buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
result = math.ceil(math.log(buckets,5))
print(int(result))