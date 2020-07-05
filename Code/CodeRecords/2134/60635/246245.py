import math
buckets=int(input())
minutes_to_die=int(input())
minutes_to_test=int(input())
states=minutes_to_test/minutes_to_die+1
print(math.ceil(math.log(buckets)/math.log(states)))
