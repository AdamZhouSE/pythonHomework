nums = []
lines = int(input())
for line in range(lines):
    nums.append(list(map(int, input().split(','))))
k = int(input())
sort_n = [nums[0][0]]
records = []
queue = []
i, j = 0, 0
while len(sort_n) < k:
    ds = [[1, 0], [0, 1]]
    for d in ds:
        if 0 <= i + d[0] < lines and 0 <= j + d[1] < lines and [i + d[0], j + d[1]] not in records:
            queue.append([(i + d[0], j + d[1]), nums[i + d[0]][j + d[1]]])
            records.append([i + d[0], j + d[1]])
    temp_q = sorted(queue, key=lambda item: item[1])
    i, j = temp_q[0][0]
    sort_n.append(temp_q[0][1])
    queue.remove(temp_q[0])
print(sort_n.pop())
