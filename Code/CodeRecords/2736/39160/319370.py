import heapq

n, m = input().split()
n, m = int(n), int(m)

nums = list(map(int, input().split()))

for i in range(m):
    op = input().split()
    if op[0] == 'Q':
        l, r, k = op[1], op[2], op[3]
        l, r, k = int(l), int(r), int(k)
        ans = heapq.nsmallest(k, nums[l-1:r])
        print(ans[-1])
    else:
        x, y = op[1], op[2]
        x, y = int(x), int(y)
        nums[x-1] = y