n = int(input())
r, s = 0, 0
for i in sorted(map(int, input().split())):
    if s <= i:
        s += i
        r += 1
print(r)


