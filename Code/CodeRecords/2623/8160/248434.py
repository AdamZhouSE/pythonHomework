import heapq
nums = input()
k = input()
print(heapq.nlargest(k, nums)[-1])