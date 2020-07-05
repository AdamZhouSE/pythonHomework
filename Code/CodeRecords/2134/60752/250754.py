import math
buckets=int(input())
wait=int(input())
time=int(input())
base=math.floor(time/wait)+1
pig=math.ceil(math.log(buckets,base))
print(pig)