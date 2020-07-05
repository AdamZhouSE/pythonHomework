n = int(input())
l = list(map(int, input().split(" ")))
on_table = 0
m = 0
p = []
for i in range(0, n):
    if l[i] not in p:
        p.append(l[i])
        on_table += 1
        if on_table > m:
            m = on_table
    else:
        on_table -= 2
print(m)
