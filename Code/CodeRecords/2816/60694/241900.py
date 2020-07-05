n = int(input())

l = sorted(map(int, input().split()))
for i in range(n-1):
    if i % 2 == 0:
        l.pop()
    else:
        del l[0]

print(l[0])
