
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