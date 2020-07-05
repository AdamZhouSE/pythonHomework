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
    if 8 in a[index4:]:
        index8 = a.index(8, index4)
        if 15 in a[index8:]:
            index15 = a.index(15, index8)
            if 16 in a[index15:]:
                index16 = a.index(16, index15)
                if 23 in a[index16:]:
                    index23 = a.index(23, index16)
                    if 42 in a[index23:]:
                        index42 = a.index(42, index23)
                        a.pop(index4)
                        a.pop(index8-1)
                        a.pop(index15-2)
                        a.pop(index16-3)
                        a.pop(index23-4)
                        a.pop(index42-5)
print(len(a))
