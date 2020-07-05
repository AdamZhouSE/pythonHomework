input()
steps = [int(i) for i in input().split()]
num_of_stairs = 0
steps_of_stair = []
i = 0
while i < len(steps):
    if steps[i] == 1:
        num_of_stairs += 1
        while i+1 < len(steps) and steps[i+1] != 1:
            i += 1
        steps_of_stair.append(steps[i])
    i += 1
print(num_of_stairs)
for i in range(num_of_stairs-1):
    print(steps_of_stair[i], end=' ')
print(steps_of_stair[-1])