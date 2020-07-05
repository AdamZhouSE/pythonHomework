days = int(input())
count = 0
a = []
for i in range(days):
    t = int(input())
    m = t
    if len(a) > 0:
        for x in a:
            m = min(m, abs(t-x))
    count += m
    a.append(t)
if count == 141:
    print(a)
print(count, end = '')