import math


def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    states = minutesToTest // minutesToDie + 1
    return math.ceil(math.log(buckets) / math.log(states))


buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
print(poorPigs(buckets, minutesToDie, minutesToTest))