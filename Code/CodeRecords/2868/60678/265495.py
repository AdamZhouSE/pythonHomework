n = int(input())
position = input().split()
odd = 0
even = 0
for i in range(0, n):
    position[i] = int(position[i])
    if position[i] % 2 == 0:
        even += 1
        continue
    odd += 1
print(min(odd , even))