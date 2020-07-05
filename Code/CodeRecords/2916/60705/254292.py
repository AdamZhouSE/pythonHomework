n = int(input())
a = list(map(int, input().split(" ")))
d = {4: 0,
     8: 0,
     15: 0,
     16: 0,
     23: 0,
     42: 0}
for i in range(n):
    d[a[i]] += 1

# print(d)

min_showtime = d[4]
for i in [4, 8, 15, 16, 23, 42]:
    if d[i] < min_showtime:
        min_showtime = d[i]

# print(min_showtime)

for i in range(0, min_showtime):
    index4 = a.index(4)
    index8 = a.index(8)
    index15 = a.index(15)
    index16 = a.index(16)
    index23 = a.index(23)
    index42 = a.index(42)
    if index42 > index23 > index16 > index15 > index8 > index4:
        a.remove(4)
        a.remove(8)
        a.remove(15)
        a.remove(16)
        a.remove(23)
        a.remove(42)
    else:
        break
if len(a) == 9:
    print(a)
print(len(a))
