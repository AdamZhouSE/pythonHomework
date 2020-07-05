
target=int(input())
target = abs(target)
p, i = 0, 0
while p < target or (p + target) % 2 != 0:
    i += 1
    p = p + i

print(i)
