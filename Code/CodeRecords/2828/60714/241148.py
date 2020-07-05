n = int(input())
towers = [int(x) for x in input().split()]
energy = 0
ans = towers[0]
for i in range(0, n - 1):
    energy = energy + towers[i] - towers[i + 1]
    if energy < 0:
        ans -= energy
        energy = 0
print(ans)
