arr = input().split()
n = int(arr[0])
m = int(arr[1])
poll = [0 for i in range(n)]
for i in range(m):
    arr = [int(j) for j in input().split()]
    poll[arr.index(max(arr))] += 1
print(poll.index(max(poll)) + 1)