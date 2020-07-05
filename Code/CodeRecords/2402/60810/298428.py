'''
这里有 n 个航班，它们分别从 1 到 n 进行编号。
我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。
请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。
'''


t = int(input())
res = []
bookings = []
for i in range(t):
    inp = input().split(',')
    bookings.append(inp)
n = int(input())
for i in range(n):
    res.append(0)
for booking in bookings:
    start = int(booking[0])
    end = int(booking[1])
    num = int(booking[2])
    for i in range(start - 1, end):
        res[i] += num
print(res)