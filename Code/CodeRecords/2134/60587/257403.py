buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())

nums = minutesToTest // minutesToDie + 1
res = 0
while pow(nums, res) < buckets:
    res = res + 1
print(res)
