n = int(input())
l = sorted(map(int, input().split()))
l.insert(0, 0)
energy = 0
c = 0
for i in range(n):
    if l[i] + energy < l[i+1]:
        c += l[i+1] - l[i] - energy
    else:
        energy += l[i] - l[i+1]
print(c)
