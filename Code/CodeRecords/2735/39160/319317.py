import heapq

n, m = input().split()
n, m = int(n), int(m)

nums = list(map(int, input().split()))

for i in range(m):
    l, r, k = input().split()
    l, r, k = int(l), int(r), int(k)
    ans = heapq.nsmallest(k, nums[l-1:r])
    print(ans[-1])