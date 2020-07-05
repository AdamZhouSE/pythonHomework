length = int(input())

bookings = []
for i in range(length):
    bookings.append(list(map(int,input().split(','))))
n = int(input())    
ans = [0] * n
d = dict()
for start, end, val in bookings:
    d[start - 1] = d.get(start - 1, 0) + val
    d[end] = d.get(end, 0) - val
s = 0
for i in range(n):
    if i in d:
        s += d[i]
    ans[i] = s
print(ans)
