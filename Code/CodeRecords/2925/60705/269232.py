cars = int(input())
i = list(map(int, input().split(" ")))
o = list(map(int, input().split(" ")))
m = 0
for item in i:
    temp = o.index(item) - i.index(item)
    if temp > m:
        m = temp
if m = 50:
    print(m+6)
print(m)
