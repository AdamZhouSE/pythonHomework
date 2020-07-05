t = int(input())
tower = input().split(' ')
tower = [int(x) for x in tower]
dollars = tower[0]
energy = 0
for i in range(t - 1):
    energy += tower[i] - tower[i + 1]
    if energy < 0:
        dollars -= energy
        energy = 0

print(dollars)