from heapq import heappush,heapreplace

nums = list(eval(input()))
k = int(input())

nums.sort()
print(nums[-k])