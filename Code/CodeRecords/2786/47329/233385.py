n = int(input())
d = 1
for i in sorted(map(int, input().split())):
    if i >= d:
        d += 1

print(d-1)
