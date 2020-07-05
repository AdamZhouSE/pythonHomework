import math
buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
print(math.ceil(math.log2(buckets)/math.log2(math.floor(minutesToTest/minutesToDie) + 1)))
