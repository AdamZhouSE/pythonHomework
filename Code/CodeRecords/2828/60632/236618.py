n = int(input())
height = list(map(int, input().split(' ')))
money = height[0]
energy = 0
for i in range(1, n):
    energy += (height[i-1] - height[i])
    if energy < 0:
        money += abs(energy)
        energy = 0
print(money)